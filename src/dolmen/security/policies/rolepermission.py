# -*- coding: utf-8 -*-

from zope.securitypolicy.interfaces import IRolePermissionManager
from zope.securitypolicy.securitymap import AnnotationSecurityMap
from zope.securitypolicy.rolepermission import RolePermissionManager


class ExtraRolePermissionMap(RolePermissionManager):

    def __init__(self, context):
        super(ExtraRolePermissionMap, self).__init__()
        self.context = context
        self.extra = self._compute_extra_data()

    def getRolesAndPermissions(self):
        return self.getAllCells() + self.extra.getAllCells()
