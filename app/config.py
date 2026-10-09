class Config:
    SECRET_KEY = "bank123"      # planted flaw: weak, hardcoded key (A02)
    DEBUG = True                # planted flaw: debug mode on (A05)