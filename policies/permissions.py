from fastapi import Depends, HTTPException, status
from core.models import User
from .roles import ROLE_PERMISSIONS
from typing import Callable

def require_permission(permission: str):
    def dependency(current_user: User = Depends()):
        user_perms = ROLE_PERMISSIONS.get(current_user.role.value, [])
        if permission not in user_perms and "*" not in user_perms:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "error": {
                        "code": "forbidden",
                        "message": "Insufficient permissions",
                        "details": None
                    }
                }
            )
        return True
    return dependency
