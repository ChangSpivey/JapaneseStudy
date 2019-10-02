#-*- coding: utf-8 -*-
import os
from aqt import mw # this script isn't imported until profile is loaded

# 4th (lowest) priority
default = {
    'path_dbs': os.path.join( mw.pm.profileFolder(), 'dbs' ),
    'path_priority': os.path.join( mw.pm.profileFolder(), 'dbs', 'priority.db' ),
    'path_ext': os.path.join( mw.pm.profileFolder(), 'dbs', 'external.db' ),
    'path_frequency': os.path.join( mw.pm.profileFolder(), 'dbs', 'frequency.txt' ),
    'path_all': os.path.join( mw.pm.profileFolder(), 'dbs', 'all.db' ),
    'path_mature': os.path.join( mw.pm.profileFolder(), 'dbs', 'mature.db' ),
    'path_known': os.path.join( mw.pm.profileFolder(), 'dbs', 'known.db' ),
    'path_seen': os.path.join( mw.pm.profileFolder(), 'dbs', 'seen.db' ),
    'path_log': os.path.join( mw.pm.profileFolder(), 'morphman.log' ),
    'path_stats': os.path.join( mw.pm.profileFolder(), 'morphman.stats' ),
    'path_analysis_input': '',         # Default path to Input directory in Readability Analyzer.
    'path_master_frequency_list': '',  # Default path to Master Frequency List in Readability Analyzer.

    # change the thresholds for various stages of maturity, in days
    'threshold_mature': 21,         # 21 days is what Anki uses
    'threshold_known': 10/86400.,   # recommend a few seconds if you want to count things in learning queue or ~3 days otherwise
    'threshold_seen': 1/86400.,     # this currently isn't used outside of create seen.db for your personal usage
    'text file import maturity':22, # when you import a file via Extract Morphemes from file, they are all given this maturity

    # change morpheme parsing
    'ignore grammar position': False, # if True, ignores morpheme grammar positions.  Delete your all.db if changing.

    # Analyzer defaults
    'default_study_target': 98.0,
    'default_morphemizer': 'MecabMorphemizer', # Options: MecabMorphemizer, SpaceMorphemizer, CjkCharMorphemizer, JiebaMorphemizer

    # reviewer mode keybindings
    'browse same focus key': 'l',
    'set known and skip key': 'k',
    'set batch play key': 'Ctrl+Alt+P',
    'set extract morphemes key': 'Ctrl+Alt+E',
    'set learn now key': 'Ctrl+Alt+N',
    'set mass tagger key': 'Ctrl+Alt+T',
    'set view morphemes key': 'Ctrl+Alt+V',
    'auto skip alternatives': True,
    'print number of alternatives skipped': True,   # after answering or skipping a card in reviewer

    # database saving/loading. you can disable these for performance reasons but their semantics are uninitutive
        # for example: features like morphHighlight always try to load all.db and expect it to be up to date
        # so not saving all.db and having it load an out of date copy many produce strange behavior
    'loadAllDb':True,   # whether to load existing all.db when recalculating or create one from scratch
    'saveDbs':True,     # whether to save all.db, known.db, mature.db, and seen.db

    # only these can have model overrides
    'set due based on mmi':True,    # whether to modify card Due times based on MorphManIndex. does nothing if relevant notes aren't enabled
    'ignore maturity':False,        # if True, pretends card maturity is always zero

    # controls for morpheme analysis (only for japanese/mecab morphemizer)
    'japanese_tag': 'japanese',              # if a note has this tag, morphemes are be split with mecab, otherwise a space-based morphemizer is used

    # try playing fields in this order when using batch media player
    'batch media fields': [ 'Video', 'Sound' ],

    # configure morph man index algorithm
    'min good sentence length': 2,
    'max good sentence length': 8,          # +1000 MMI per morpheme outside the "good" length range
    'reinforce new vocab weight': 5.0,      # -reinforce_weight / maturity MMI per known that is not yet mature
    'verb bonus': 100,                      # -verb_bonus if at least one unknown is a verb
    
    # -priority_weight per unknown that exists in priority.db
    'priority.db weight': 200,
    
    # Scale by which card "due" values decrease per unknown in frequency.txt
    # Lower the scale based on the size of frequency.txt
    # Example: 10k frequency.txt scale: 2; 5k frequency.txt scale: 4
    'frequency.txt weight scale': 10, 

    # only these can have deck overrides
    'next new card feature':True,   # skip cards with focusMorph that was already seen or aren't k+1
    'new card merged fill':False,   # fill new card queue with cards from all child decks instead of sequentially. also enforce a minimum due value
    'new card merged fill min due':100000,   # k+1 by default. this mostly is to boost performance of 'next new card feature'
}
# Can override anything. 3rd priority
profile_overrides = {
}

# Model overrides can only override the entries marked above. 2nd priority
model_overrides = {
    'JtMW':             { 'set due based on mmi': False, 'ignore maturity': True },
    'JSPfEC':           { 'set due based on mmi': False },
    'Tae Kim Cloze':    { 'set due based on mmi': False },
    'Yotsubato':        { 'set due based on mmi': True },
    'Rikaisama':        { 'set due based on mmi': False },
   #'Kore':             { 'set due based on mmi': False, 'morph_fields':[u'SentenceExpression'] },
    'Kore':             { 'set due based on mmi': False },
}

# Deck overrides can only override 'new card merged fill' options. 1st priority
deck_overrides = {
    'Sentences':            { 'new card merged fill':True },
    'Sentences::subs2srs':  { 'new card merged fill':True },
    'Sentences::vn2srs':    { 'new card merged fill':True },
    'ExtraVocab':           { 'new card merged fill':True },
    'ExtraVocab::_Yotsubato':   { 'new card merged fill':True },
    'ExtraVocab::_Kore':        { 'new card merged fill':True },
}
