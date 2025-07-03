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

from pydantic import BaseModel, ValidationError, field_validator
from typing import List, Dict
import regex

#Status Information
class StatusInfo(BaseModel):
    status:str
    message:str

class TransversalState(BaseModel):
    userId: str
    roleId: int
    username: str
    csrfToken: str
    
'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.regist.model
'''
class Reference(BaseModel):
    url:str
    surface:str 
    surfaceIndex: int
    isWholeSentence:bool
    originalUrlOrReference:str
    metaInformations:List[str]

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.regist.model
'''
class ImageReference(BaseModel):
    reference:Reference
    x:int
    y:int
    width:int 
    height:int

class TableReference(BaseModel):
    reference:Reference

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.regist.model
'''
class KnowledgeForImage(BaseModel):
    id:str
    imageReference:ImageReference


class KnowledgeForTable(BaseModel):
    id:str
    tableReference:TableReference

class DocumentPageReference(BaseModel):
    pageNo:int
    references:List[str] = []
    tableOfContents:List[str] = []
    headlines:List[str] = []

class KnowledgeForDocument(BaseModel):
    id:str
    filename:str
    url:str
    titleOfTopPage:str

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.regist.model
'''
class Knowledge(BaseModel):
    sentence:str
    lang:str
    extentInfoJson:str
    isNegativeSentence:bool = False
    knowledgeForImages:List[KnowledgeForImage] = []
    knowledgeForTables:List[KnowledgeForTable] = []
    knowledgeForDocument:KnowledgeForDocument = KnowledgeForDocument(id="", filename="", url="", titleOfTopPage="")   
    documentPageReference: DocumentPageReference = DocumentPageReference(pageNo = -1, references = [], tableOfContents = [])

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class KnowledgeFeatureReference(BaseModel):
    id:str 
    featureType:int 
    url:str = ""
    source:str = ""
    featureInputType:int = 0    
    extentText:str = "{}"

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class LocalContext(BaseModel):
    lang: str
    namedEntity: str
    rangeExpressions: dict
    categories: dict
    domains: dict
    knowledgeFeatureReferences:List[KnowledgeFeatureReference]

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class PredicateArgumentStructure(BaseModel):
    currentId:int
    parentId:int
    isMainSection:bool
    surface:str
    normalizedName:str
    dependType:str
    caseType:str
    isDenialWord:bool
    isConditionalConnection:bool
    normalizedNameYomi:str
    surfaceYomi:str
    modalityType:str
    parallelType:str
    nodeType:int
    morphemes:List[str]

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class KnowledgeBaseNode(BaseModel):
    nodeId:str
    propositionId:str
    sentenceId:str
    predicateArgumentStructure:PredicateArgumentStructure
    localContext:LocalContext

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class KnowledgeBaseEdge(BaseModel):
    sourceId:str
    destinationId:str 
    caseStr:str
    dependType:str
    parallelType:str
    hasInclusion:bool
    logicType:str

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class LocalContextForFeature(BaseModel):
    lang: str
    knowledgeFeatureReferences:List[KnowledgeFeatureReference]

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class KnowledgeBaseSemiGlobalNode(BaseModel):
    sentenceId: str
    propositionId: str
    documentId: str
    sentence: str
    sentenceType:int
    localContextForFeature: LocalContextForFeature

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.model
'''
class KnowledgeBaseGlobalNode(BaseModel):
    documentId: str
    filename:str
    url:str 
    titleOfTopPage:str
    totalPageNum:int

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class MatchedFeatureInfo(BaseModel):
    featureId:str
    similarity:float

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class CoveredPropositionNode(BaseModel):    
    terminalId:str
    terminalSurface:str
    terminalUrl:str

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class CoveredPropositionEdge(BaseModel):
    sourceNode:CoveredPropositionNode
    destinationNode:CoveredPropositionNode

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class KnowledgeBaseSideInfo(BaseModel):
    propositionId:str
    sentenceId:str
    featureInfoList:List[MatchedFeatureInfo]


'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class CoveredPropositionResult(BaseModel):
    deductionUnit:str
    propositionId:str 
    sentenceId:str
    coveredPropositionEdges:List[CoveredPropositionEdge]
    knowledgeBaseSideInfo:List[KnowledgeBaseSideInfo]

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class DeductionResult(BaseModel):
    status:bool 
    coveredPropositionResults:List[CoveredPropositionResult]
    havePremiseInGivenProposition:bool = False

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class AnalyzedSentenceObject(BaseModel):
    nodeMap:Dict[str, KnowledgeBaseNode]
    edgeList:List[KnowledgeBaseEdge]
    knowledgeBaseSemiGlobalNode:KnowledgeBaseSemiGlobalNode
    deductionResult:DeductionResult

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.base
'''
class AnalyzedSentenceObjects(BaseModel):
    analyzedSentenceObjects:List[AnalyzedSentenceObject]

class Propositions(BaseModel):
    propositions: List[List[Knowledge]]


'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.parser
'''
class InputSentence(BaseModel):
    premise:List[Knowledge] 
    claim:List[Knowledge]


'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.parser
'''
class KnowledgeForParser(BaseModel):
    propositionId:str
    sentenceId:str
    knowledge:Knowledge

'''
ref. https://github.com/toposoid/toposoid-deduction-protocol-model
com.ideal.linked.toposoid.protocol.model.parser
'''
class InputSentenceForParser(BaseModel):
    premise:List[KnowledgeForParser] 
    claim:List[KnowledgeForParser]


'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.nlp.model
'''
class SingleSentence(BaseModel):
    sentence: str

'''
ref. https://github.com/toposoid/toposoid-knowledgebase-model
com.ideal.linked.toposoid.knowledgebase.nlp.model
'''
class SurfaceInfo(BaseModel):
   surface: str
   index: int 

class DetectedLanguage(BaseModel):
    lang: str

###DOCUMENT-ANALYSIS-SUBSCRIBER###
class Document(BaseModel):
    documentId: str
    filename: str
    url: str 
    size:int

class DocumentRegistration(BaseModel):
    document:Document
    transversalState:TransversalState

###REDIS####
class KeyValueStoreInfo(BaseModel):
    identifier: str
    key: str
    value: str

###MYSQL####
class DocumentAnalysisResultHistoryRecord(BaseModel):
    stateId: int
    documentId: str
    originalFilename: str
    totalSeparatedNumber: int

class KnowledgeRegisterHistoryRecord(BaseModel):
    stateId:int
    documentId:str 
    sequentialNumber:int
    propositionId:str
    sentences:str
    json:str    

class KnowledgeRegisterHistoryCount(BaseModel):
    documentId:str
    count:int

###FEATURE_VECTOR###
#For deleting feature vectors
class FeatureVectorIdentifier(BaseModel):
    superiorId:str
    featureId:str
    sentenceType:int
    lang:str
    superiorType:int
    nonSentenceType: int

    @field_validator("superiorId", mode='before')
    def parseSuperiorId(cls, v):
        if not isinstance(v, str):            
            raise ValidationError("superiorId is not StringType.")
        return v

    @field_validator("featureId", mode='before')
    def parseFeatureId(cls, v):
        if not isinstance(v, str):            
            raise ValidationError("featureId is not StringType.")
        return v

    @field_validator("sentenceType", mode='before')
    def parseSentenceType(cls, v):
        if not isinstance(v, int):            
            raise ValidationError("sentenceType is not IntType.")
        return v

    @field_validator("lang", mode='before')
    def parseLang(cls, v):
        if not isinstance(v, str):            
            raise ValidationError("lang is not StringType.")
        return v

    @field_validator("superiorType", mode='before')
    def parseSuperiorType(cls, v):
        if not isinstance(v, int):            
            raise ValidationError("superiorType is not IntType.")
        return v

    @field_validator("nonSentenceType", mode='before')
    def parseNonSentenceType(cls, v):
        if not isinstance(v, int):            
            raise ValidationError("nonSentenceType is not IntType.")
        return v


    @field_validator("superiorId")
    def isNotEmptyPropositionId(cls, v):
        if not v:
            raise ValidationError("propositionId is empty.")
        return v

    @field_validator("featureId")
    def isNotEmptyFeatureId(cls, v):
        if not v:
            raise ValidationError("featureId is empty.")
        return v

    @field_validator("sentenceType")
    def isNotEmptySentenceType(cls, v):
        if v > 6 or v < -1:
            raise ValidationError("sentenceType is invalid.")
        return v

    @field_validator("lang")
    def isNotEmptyLang(cls, v):
        if not v:
            raise ValidationError("lang is empty.")
        if v not in ["ja_JP", "en_US"] and not regex.search(r"^@@_#[0-9]+", v):
            raise ValidationError("lang is invalid.")
        return v
    
    @field_validator("superiorType")
    def isNotEmptySuperiorType(cls, v):
        if v < 0:
            raise ValidationError("superiorType is invalid.")
        return v

    @field_validator("nonSentenceType")
    def isNotEmptyNonSentenceType(cls, v):
        if v < 0:
            raise ValidationError("nonSentenceType is invalid.")
        return v

#For searching feature vectors.
class FeatureVectorForUpdate(BaseModel):
    featureVectorIdentifier: FeatureVectorIdentifier
    vector:List[float]

#For feature vector search requests
class SingleFeatureVectorForSearch(BaseModel):
    vector:List[float]
    num:int

#For feature vector search requests
class SingleFeatureVectorForEasySearch(BaseModel):
    vector:List[float]
    num:int
    similarityThreshold:float

#For feature vector search results
class FeatureVectorSearchResult(BaseModel):
    ids:List[FeatureVectorIdentifier]
    similarities:List[float]
    statusInfo:StatusInfo

class PropositionRelation(BaseModel):
    operator:str 
    sourceIndex:int 
    destinationIndex:int

class KnowledgeSentenceSet(BaseModel):
    premiseList:List[Knowledge]
    premiseLogicRelation:List[PropositionRelation]
    claimList:List[Knowledge]
    claimLogicRelation:List[PropositionRelation]


class NormalizedWord(BaseModel):
    word:str

class SynonymList(BaseModel):
    synonyms:List[str]

class FeatureVector(BaseModel):
    vector:List[float]

class SingleImage(BaseModel):
    url:str
