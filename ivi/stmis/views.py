# -*- coding: utf-8 -*-
"""STMIS application views."""
from flask import Blueprint, render_template

mod = Blueprint('stmis', __name__, url_prefix='/stmis', static_folder='../static')


@mod.route('/')
def index():
    """List of reports"""
    return render_template('stmis/index.html')
