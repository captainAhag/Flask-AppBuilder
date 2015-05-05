from flask_babelpkg import lazy_gettext

"""
	All constants and messages definitions go here

	Log messages obey the following rule:
		
		LOGMSG_<SEV>_<MODULE>_<NAME>
			<SEV> :- INF | DEB | WAR | ERR
			<MODULE> :- SEC

	Flash messages obey the following rule:
		
		FLAMSG_<SEV>_<MODULE>_<NAME>
			<SEV> :- INF | DEB | WAR | ERR
			<MODULE> :- SEC

"""

LOGMSG_ERR_SEC_ACCESS_DENIED = "Access is Denied for: {0} on: {1}"
""" Access denied log message, format with user and view/resource """
LOGMSG_ERR_SEC_CREATE_DB = "DB Creation and initialization failed: {0}"
""" security models creation fails, format with error message """
LOGMSG_ERR_SEC_ADD_ROLE = "Add Role: {0}"
""" Error adding role, format with err message """
LOGMSG_ERR_SEC_ADD_PERMISSION = "Add Permission: {0}"
""" Error adding permission, format with err message """
LOGMSG_ERR_SEC_ADD_VIEWMENU = "Add View Menu Error: {0}"
""" Error adding view menu, format with err message """
LOGMSG_ERR_SEC_DEL_PERMISSION = "Del Permission Error: {0}"
""" Error deleting permission, format with err message """
LOGMSG_ERR_SEC_ADD_PERMVIEW = "Creation of Permission View Error: {0}"
""" Error adding permission view, format with err message """
LOGMSG_ERR_SEC_DEL_PERMVIEW = "Remove Permission from View Error: {0}"
""" Error deleting permission view, format with err message """
LOGMSG_ERR_SEC_ADD_PERMROLE = "Add Permission to Role Error: {0}"
""" Error adding permission to role, format with err message """
LOGMSG_ERR_SEC_DEL_PERMROLE = "Remove Permission to Role Error: {0}"
""" Error deleting permission to role, format with err message """
LOGMSG_WAR_SEC_NO_USER = "No user yet created, use fabmanager command to do it."
""" Warning when app starts if no user exists on db """
LOGMSG_INF_SEC_ADD_PERMVIEW = "Created Permission View: {0}"
""" Info when adding permission view, format with permission view class string """
LOGMSG_INF_SEC_DEL_PERMVIEW = "Removed Permission View: {0}"
""" Info when deleting permission view, format with permission view class string """
LOGMSG_INF_SEC_ADD_PERMROLE = "Added Permission {0} to role {1}"
""" Info when adding permission to role, format with permission view class string and role name """
LOGMSG_INF_SEC_DEL_PERMROLE = "Removed Permission {0} to role {1}"
""" Info when deleting permission to role, format with permission view class string and role name """
LOGMSG_INF_SEC_ADD_ROLEADMIN = "Inserted Role for Admin access {0}"
""" Info when added the role admin, format with role name """
LOGMSG_INF_SEC_ADD_ROLEPUBLIC = "Inserted Role for public access %s"
""" Info when added the role public, format with role name """
LOGMSG_INF_SEC_NO_DB = "Security DB not found Creating all Models from Base"
LOGMSG_INF_SEC_ADD_DB = "Security DB Created"

LOGMSG_ERR_FAB_ADD_PERMISSION_MENU = "Add Permission on Menu Error: {0}"
""" Error when adding a permission to a menu, format with err """
LOGMSG_ERR_FAB_ADD_PERMISSION_VIEW = "Add Permission on View Error: {0}"
""" Error when adding a permission to a menu, format with err """
LOGMSG_ERR_DBI_ADD_GENERIC = "Add record error: {0}"
""" Database add generic error, format with err message """
LOGMSG_ERR_DBI_EDIT_GENERIC = "Edit record error: {0}"
""" Database edit generic error, format with err message """
LOGMSG_ERR_DBI_DEL_GENERIC = "Delete record error: {0}"
""" Database delete generic error, format with err message """

LOGMSG_WAR_FAB_VIEW_EXISTS = "View already exists {0} ignoring"
""" Attempt to add an already added view, format with view name """
LOGMSG_WAR_DBI_ADD_INTEGRITY = "Add record integrity error: {0}"
""" Dabase integrity error, format with err message """
LOGMSG_WAR_DBI_EDIT_INTEGRITY = "Edit record integrity error: {0}"
""" Dabase integrity error, format with err message """
LOGMSG_WAR_DBI_DEL_INTEGRITY = "Delete record integrity error: {0}"
""" Dabase integrity error, format with err message """

LOGMSG_INF_FAB_ADD_VIEW = "Registering class {0} on menu {1}"
""" Inform that view class was added, format with class name, name"""



FLAMSG_ERR_SEC_ACCESS_DENIED = lazy_gettext("Access is Denied")
""" Access denied flash message """


PERMISSION_PREFIX = 'can_'
""" Prefix to be concatenated to permission names, and inserted in the backend """

AUTH_OID = 0
AUTH_DB = 1
AUTH_LDAP = 2
AUTH_REMOTE_USER = 3
AUTH_OAUTH = 4
""" Constants for supported authentication types """
