#!/usr/bin/env python
# coding: utf-8

# # Bluecoats Phase 1 Config File
# * Organization-level configuration; modify according to specific organization-level goals and stakeholder requirements
# * Values in this file are largely constants and should not change often or significanctly

# ## Organization

# In[1]:


ORG_ID = 'UPHS'
ORG_NAME = 'University of Pennsylvania Health System'
ORG_TZ = 'US/Eastern'


# ## Paths

# In[ ]:


PROJECT_PATH = '/' # replace as needed

DATA_PATH = PROJECT_PATH + 'data/'
OUTPUT_PATH = PROJECT_PATH + 'output/'
LOG_PATH = PROJECT_PATH + 'logs/'
ARCHIVE_PATH = PROJECT_PATH + 'archive/'

RAW_DATA_PATH = DATA_PATH + 'raw_data/'
RAW_SCORE_PATH = RAW_DATA_PATH + 'score_survey/'
RAW_ENGAGEMENT_PATH = RAW_DATA_PATH + 'engagement/'
RAW_BUDGETING_PATH = RAW_DATA_PATH + 'budgeting/'
RAW_SUPPLIES_PATH = RAW_DATA_PATH + 'supplies/'
RAW_HTB_PATH = RAW_DATA_PATH + 'htb/'

MASTER_DATA_PATH = DATA_PATH + 'master_data/'
MASTER_SCORE_PATH = MASTER_DATA_PATH + 'score_survey/'
MASTER_ENGAGEMENT_PATH = MASTER_DATA_PATH + 'engagement/'
MASTER_BUDGETING_PATH = MASTER_DATA_PATH + 'budgeting/'
MASTER_SUPPLIES_PATH = MASTER_DATA_PATH + 'supplies/'
MASTER_HTB_PATH = MASTER_DATA_PATH + 'htb/'

FIGURE_PATH = OUTPUT_PATH + 'figures/'
CHART_PATH = OUTPUT_PATH + 'charts/'
REPORT_PATH = OUTPUT_PATH + 'reports/'


# ## Visualization

# In[ ]:


# Flow-based figures
NODE_ALPHA = '0.8'
LINK_ALPHA = '0.2'
DEFAULT_ALPHA = '0.5'

# Common colors
RGB_GREY = '192,192,192'
RGB_RED = '255,0,0'
RGB_GREEN = '0,255,0'
RGB_BLUE = '0,0,255'
RGB_ORANGE = '255,128,0'
RGB_MAGENTA = '204,0,102'

# Default save params
SAVE_DPI = 500


# In[ ]:


# Text color and emphasis
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# ## Project Specific

# ### Supply Room - Dedicated Staff Position

# In[ ]:


SUPPLY_STAFF_ID = '159215' 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




