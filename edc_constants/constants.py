import re

ADDITIONAL = True
ABNORMAL = 'ABNORMAL'
AFTERNOON = 'afternoon'
ALIVE = 'alive'
ANYTIME = 'anytime'
BY_BIRTH = 'BY_BIRTH'
CLOSED = 'closed'
COMPLETE = 'COMPLETE'
CONSENTED = 'CONSENTED'
CONTINUOUS = 'continuous'
DEAD = 'dead'
DECLINED = 'Declined'
DEFAULTER = 'defaulter'
DELETE = 'DELETE'
DONE = 'done'
DONT_KNOW = 'dont_know'
DWTA = 'DWTA'  # don't want to answer'
ERROR = 'ERROR'
EVENING = 'evening'
FAILED_ELIGIBILITY = 'failed eligibility'
FEMALE = 'F'
HIDE_FORM = 'NOT_REQUIRED'
INCOMPLETE = 'INCOMPLETE'
IND = 'IND'
INSERT = 'INSERT'
MALE = 'M'
MORNING = 'morning'
NAIVE = 'NAIVE'
NEG = 'NEG'
NEVER = 'NEVER'
NEW = 'New'
NO = 'No'
NONE = 'none'
NORMAL = 'NORMAL'
NOT_ADDITIONAL = False
NOT_APPLICABLE = 'N/A'
NOT_EVALUATED = 'Not evaluated'
NOT_SURE = 'not_sure'
OFF_STUDY = 'off study'
OFF_STUDY_VISIT = 'off study'
OMANG = 'OMANG'
ON_ART = 'on_art'
ON_STUDY = 'on study'
OPEN = 'open'
OPTIONAL = True
OTHER = 'OTHER'
PARTIAL = 'PARTIAL'
PARTICIPANT = 'participant'
PENDING = 'PENDING'
POS = 'POS'
PRINT = 'PRINT'
QUERY = 'QUERY'
REFUSED = 'REFUSED'
RESTARTED = 'restarted'
SCREENED = 'SCREENED'
SEROCONVERSION = 'seroconversion'
SHOW_FORM = 'NEW'
STOPPED = 'stopped'
SUBJECT = 'subject'
UNK = 'UNK'
UNKNOWN = 'unknown'
UPDATE = 'UPDATE'
UUID_PATTERN = re.compile(
    '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}')
VIEW = 'VIEW'
WEEKDAYS = 'weekdays'
WEEKENDS = 'weekends'
YES = 'Yes'
