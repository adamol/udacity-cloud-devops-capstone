TODO:
- add on_fail docker prune
- pytest
    + accept query params
    + default to Mumu
- docker credentials token

Extra:
- cloudformation
    + cloudwatch cron -> SQS
    + SQS <- lambda [generate string] -> API call
    + get emails list from dynamodb -> send mails with cow
