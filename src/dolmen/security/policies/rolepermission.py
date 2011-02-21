# -*- coding: utf-8 -*-

from zope.securitypolicy.interfaces import IRolePermissionManager
from zope.securitypolicy.securitymap import AnnotationSecurityMap
from zope.securitypolicy.rolepermission import RolePermissionManager


class ExtraRolePermissionMap(RolePermissionManager):

    def __init__(self, context):
        super(ExtraRolePermissionMap, self).__init__()
        self.context = context
        self.extra = self._compute_extra_data()

    def getAllCells(self):
        res = []
        for r in self._byrow.keys():
            for c in self._byrow[r].items():
                res.append((r,) + c)
        res.extend(self.extra.getAllCells())
        return res

    def queryCell(self, rowentry, colentry, default=None):
        cell = self.extra.queryCell(rowentry, colentry, default=default)
        if cell is default:
            return AnnotationPrincipalRoleManager.queryCell(
                self, rowentry, colentry, default=default)
        return cell

    def getCol(self, colentry):
        col = self.extra._bycol.get(colentry)
        former = self._bycol.get(colentry)
        if former:
            col.update(former)
        if col:
            return col.items()
        return []

    def getRow(self, rowentry):
        row = self.extra._byrow.get(rowentry)
        row.extend(self._byrow.get(rowentry))
        if row:
            return row.items()
        return []

