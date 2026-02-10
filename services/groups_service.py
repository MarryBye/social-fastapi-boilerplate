from fastapi import Depends
from database.repositories.groups_repo import GroupsRepository

class GroupsService:
    def __init__(self, groups_repo: GroupsRepository = Depends()):
        self.groups_repo = groups_repo