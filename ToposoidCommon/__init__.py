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

from .LogUtils import LogUtils
from .LangUtils import detectLangage
from .model import Knowledge, KnowledgeForDocument, DocumentPageReference, KnowledgeForTable, KnowledgeForImage, TableReference, ImageReference, Reference, KnowledgeSentenceSet, PropositionRelation
from .model import StatusInfo, TransversalState, KeyValueStoreInfo
from .model import DeductionConfiguration, AnalyzedSentenceObjects, AnalyzedSentenceObject, DeductionResult, CoveredPropositionResult, KnowledgeBaseSideInfo, CoveredPropositionEdge, MatchedKnowledgeNode, CoveredPropositionNode, MatchedFeatureInfo
from .model import KnowledgeBaseGlobalNode, KnowledgeBaseSemiGlobalNode, LocalContextForFeature, KnowledgeBaseEdge, KnowledgeBaseNode, PredicateArgumentStructure, LocalContext, KnowledgeFeatureReference
from .model import InputSentence, KnowledgeForParser, InputSentenceForParser, SingleSentence, SurfaceInfo
from .model import NormalizedWord, SynonymList, FeatureVector, SingleImage
from .constants import CaseGroupType, DataEntryType, FeatureType, NonSentenceType, ScopeType, SentenceType, SuperiorType, DeductionPhaseType, ActionModeType, AuthenticityType
__all__ = ['LogUtils', 'Knowledge', 'KnowledgeForDocument', 'DocumentPageReference', 'DocumentReference', 'KnowledgeForTable', 'KnowledgeForImage', 'TableReference', 'ImageReference', 'Reference', 'KnowledgeSentenceSet', 'PropositionRelation', 'StatusInfo', 'TransversalState', 'KeyValueStoreInfo', 'DeductionConfiguration', 'AnalyzedSentenceObjects', 'AnalyzedSentenceObject', 'DeductionResult', 'CoveredPropositionResult', 'KnowledgeBaseSideInfo', 'MatchedKnowledgeNode', 'CoveredPropositionEdge', 'CoveredPropositionNode', 'MatchedFeatureInfo', 'KnowledgeBaseGlobalNode', 'KnowledgeBaseSemiGlobalNode', 'LocalContextForFeature', 'KnowledgeBaseEdge', 'KnowledgeBaseNode', 'PredicateArgumentStructure', 'LocalContext', 'KnowledgeFeatureReference', 'InputSentence', 'KnowledgeForParser', 'InputSentenceForParser', 'SingleSentence', 'SurfaceInfo', 'DetectedLanguage', 'detectLangage', 'NormalizedWord', 'SynonymList', 'FeatureVector', 'SingleImage', 'CaseGroupType', 'DataEntryType', 'FeatureType', 'NonSentenceType', 'ScopeType', 'SentenceType', 'SuperiorType', 'DeductionPhaseType', 'ActionModeType', 'AuthenticityType']

