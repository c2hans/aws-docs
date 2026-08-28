---
source_url: https://docs.aws.amazon.com/polly/latest/dg/ListLexiconSamplePython.html
---

# ListLexicon
<a name="ListLexiconSamplePython"></a>

The following Python code example uses the AWS SDK for Python (Boto) to list the lexicons in your account in the region specified in your local AWS configuration. For information about creating the configuration file, see [Setting up the AWS CLI](setup-cli.md).

For more information on this operation, see the reference for the [`ListLexicons`](https://docs.aws.amazon.com/polly/latest/APIReference/API_ListLexicons.html) API.

```
import sys

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

# Create a client using the credentials and region defined in the adminuser
# section of the AWS credentials and configuration files
session = Session(profile_name="adminuser")
polly = session.client("polly")

try:
    # Request the list of available lexicons
    response = polly.list_lexicons()
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

# Get the list of lexicons in the response
lexicons = response.get("Lexicons", [])
print("{0} lexicon(s) found".format(len(lexicons)))

# Output a formatted list of lexicons with some of the attributes
for lexicon in lexicons:
    print((u" - {Name} ({Attributes[LanguageCode]}), "
           "{Attributes[LexemesCount]} lexeme(s)").format(**lexicon))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
