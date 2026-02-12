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