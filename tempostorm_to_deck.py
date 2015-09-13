#!/usr/bin/env python
# -*- coding: utf-8 -*-

cCount = 0
with open('tempostorm.html','r') as f:
    cardsplitter = '<div class="db-deck-card ng-scope multi" ng-class="'
    cardsplitter = '<div class="db-deck-card ng-scope" ng-class="'
    cardsplitter = '<div class="db-deck-card ng-scope'
    s = str(f.read()).split(cardsplitter)
    divdiv = '</div></div>'
    cardtitlesplit = 'div class="db-deck-card-name ng-binding">'
    for spl in s:
        if cardtitlesplit in spl:
            cardnametoedit = spl.split(cardtitlesplit)[1][:100]
            cardName = None
            if divdiv in cardnametoedit:
                cardName = cardnametoedit.split(divdiv)[0]
            else:
                continue

            if '<div class="db-deck-card-qty ng-binding" ng-show="item.qty > 1">2</div>' in spl:
                print cardName + ' × 2'
                cCount += 2
            else:
                print cardName
                cCount += 1

print '[Finished in ' + str(cCount)

