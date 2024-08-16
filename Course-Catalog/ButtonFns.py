#################################################################
# ButtonFns.py                                                  #
#                                                               # 
# This file takes care of enabling/disabling and showing/hiding #
# various HTML elements throughout the main code.               #
#################################################################


from dash import set_props
from AppLayout import visible, invisible


def enableRegistration():
    set_props('registration-button', {'disabled':False})


def disableRegistration():
    set_props('registration-button', {'disabled':True})


def enableDereg():
    set_props('deregistration-button', {'disabled':False})


def disableDereg():
    set_props('deregistration-button', {'disabled':True})


def enableAudit():
    set_props('audit-button', {'disabled':False})


def disableAudit():
    set_props('audit-button', {'disabled':True})


def showCreateStudent():
    set_props('create-student', {'hidden':False})


def hideCreateStudent():
    set_props('create-student', {'hidden':True})


def showCreateStudentText():
    set_props('create-student-text', {'hidden':False})


def hideCreateStudentText():
    set_props('create-student-text', {'hidden':True})


def showAudit():
    set_props('audit-completion', {'style':visible})
    set_props('audit-remaining', {'style':visible})


def hideAudit():
    set_props('audit-completion', {'style':invisible})
    set_props('audit-remaining', {'style':invisible})
        
