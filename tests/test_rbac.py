import pytest
from fastapi import HTTPException
from policies.permissions import require_permission
from core.models import User, RoleEnum

class DummyDepends:
    def __init__(self, role):
        self.role = role
        self.value = role

@pytest.mark.parametrize("role,perm,should_pass", [
    (RoleEnum.VIEWER, "read:dashboard", True),
    (RoleEnum.VIEWER, "read:transactions", False),
    (RoleEnum.ANALYST, "read:transactions", True),
    (RoleEnum.ADMIN, "delete:user", True),
])
def test_rbac_enforcement(role, perm, should_pass):
    user = User(username="u", email="e@e.com", password_hash="x", role=role)
    dep = require_permission(perm)
    if should_pass:
        assert dep(current_user=user) is True
    else:
        with pytest.raises(HTTPException):
            dep(current_user=user)
