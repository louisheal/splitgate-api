from flask import Flask, jsonify, request
import requests

@app.route('/')
def home():
    return "Hello world!"
