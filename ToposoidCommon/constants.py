'''
  Copyright (C) 2025  Linked Ideal LLC.[https://linked-ideal.com/]
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, version 3.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
 
  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from enum import Enum

class CaseGroupType(Enum):
    UNSPECIFIED = 0
    PREDICATE_GROUP = 1
    SUBJECT_GROUP = 2
    OBJECT_GROUP = 3

class DataEntryType(Enum):
    MANUAL = 0
    BATCH = 1

class FeatureType(Enum):
    SENTENCE = 0
    IMAGE = 1
    TABLE = 2
    SYNONYM = 3
    PREDICATE_ARGUMENT = 4
    DOCUMENT = 5
    NON_SENTENCE = 6
    CASE_PHRASE = 7

class NonSentenceType(Enum):
    UNSPECIFIED = 0
    REFERENCES = 1
    TABLE_OF_CONTENTS = 2
    HEADLINES = 3
    TITLE_OF_TOP_PAGE = 4

class ScopeType(Enum):
    LOCAL = 0
    SEMIGLOBAL = 1
    GLOBAL = 2

class SentenceType(Enum):
    PREMISE = 0
    CLAIM = 1

class SuperiorType(Enum):
    PROPOSITION_ID = 0
    DOCUMENT_ID = 1

class DeductionPhaseType(Enum):
    DEDUCTION_TERM_BASE = 1
    DEDUCTION_PHRASE_BASE = 2
    DEDUCTION_SENTENCE_BASE = 3

class ActionModeType(Enum):
    UNSPECIFIED = 0
    REGISTRATION_MODE = 1
    DEDUCTION_MODE = 2
    