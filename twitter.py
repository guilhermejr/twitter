#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, sys

# --- Texto passado como parâmetro ---
texto = str(sys.argv[1])

# --- Tamanho do texto ---
tamanho = len(texto)

# --- Verifica se o texto está no tamanho máximo de 140 caracteres ---
if tamanho > 140:
    print 'Texto muito grande (%d) para ser twitado.' % tamanho
    sys.exit(1)

# --- Variáveis de acesso ---
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS_KEY'
ACCESS_SECRET = 'ACCESS_SECRET'

# --- Acessa e envia mensagem ---
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(texto)