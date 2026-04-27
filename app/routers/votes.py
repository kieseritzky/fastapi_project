from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, database, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/votes",
    tags=["votes"]
)

@router.post("", status_code=status.HTTP_201_CREATED)
def do_vote(vote: schemas.Vote, db: Session=Depends(database.get_db),
            current_user: str = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post doesnot exist")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Post.owner_id == current_user.id)
    found_vote = vote_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {vote.post_id} was not found')


    if vote.dir==1:
        if  found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Already voted')
        else:
            new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
            db.add(new_vote)
            db.commit()

            return {"message": "vote added successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='No need to delete')
        else:
            vote_query.delete(synchronize_session=False)
            db.commit()

            return {"message": "Deleted successfully"}

