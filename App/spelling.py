from flask_cors import CORS
from flask import flask, request, render_template, redirect, flash, url_for, jsonify
from sqlalchemy.exc import IntegrityError
from models import db, Word

