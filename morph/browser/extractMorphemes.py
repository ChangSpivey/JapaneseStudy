#-*- coding: utf-8 -*-
import os
from anki.hooks import addHook
from anki.utils import stripHTML
from ..morphemes import AnkiDeck, MorphDb, getMorphemes, ms2str
from ..morphemizer import getMorphemizerByName
from ..util import addBrowserNoteSelectionCmd, mw, getFilter, infoMsg, QFileDialog, acfg

def pre( b ):
    from ..util import dbsPath # not defined until late, so don't import at top of module
    path = QFileDialog.getSaveFileName( caption='Save morpheme db to:', directory=dbsPath + os.sep + 'exportedMorphs.db' )[0]
    if not path: return
    return { 'dbpath':str(path), 'morphDb':MorphDb() }

def per( st, n ):
    mats = mw.col.db.list( 'select ivl from cards where nid = :nid', nid=n.id )
    notecfg = getFilter(n)
    if notecfg is None: return st
    morphemizer = getMorphemizerByName(notecfg['Morphemizer'])
    for f in notecfg['Fields']:
        ms = getMorphemes(morphemizer, stripHTML(n[f]), n.tags)
        loc = AnkiDeck(n.id, f, n[f], n.guid, mats)
        st['morphDb'].addMsL(ms, loc)

    return st

def post( st ):
    st['morphDb'].save( st['dbpath'] )
    infoMsg( 'DB saved with extracted morphemes' )

def runExtractMorphemes():
    label = 'MorphMan: Extract Morphemes'
    tooltipMsg = 'Extract morphemes in selected notes to a MorphMan db'
    shortcut = acfg('shortcuts', 'extractMorphemes')
    addBrowserNoteSelectionCmd( label, pre, per, post, tooltip=tooltipMsg, shortcut=(shortcut,) )

addHook( 'profileLoaded', runExtractMorphemes )
