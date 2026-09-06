---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_partnercentral-selling_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Partner Central examples using SDK for Python (Boto3)
<a name="python_3_partnercentral-selling_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Partner Central.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Actions
<a name="actions"></a>

### `AssignOpportunity`
<a name="partnercentral-selling_AssignOpportunity_python_3_topic"></a>

The following code example shows how to use `AssignOpportunity`.

**SDK for Python (Boto3)**
Reassign an existing Opportunity to another user.

```
#!/usr/bin/env python

"""
Purpose
PC-API-07 Assigning a new owner
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def assign_opportunity(identifier):
    assign_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "Identifier": identifier,
        "Assignee": {
            "BusinessTitle": "OpportunityOwner",
            "Email": "test@test.com",
            "FirstName": "John",
            "LastName": "Doe"
        }
    }
    try:
        # Perform an API call
        response = partner_central_client.assign_opportunity(**assign_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    identifier = "O4236468"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Assigning a new owner to an opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(assign_opportunity(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [AssignOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/AssignOpportunity) in *AWS SDK for Python (Boto3) API Reference*.

### `AssociateOpportunity`
<a name="partnercentral-selling_AssociateOpportunity_python_3_topic"></a>

The following code example shows how to use `AssociateOpportunity`.

**SDK for Python (Boto3)**
Create a formal association between an Opportunity and various related entities.

```
#!/usr/bin/env python

"""
Purpose
PC-API -11 Associating a product
PC-API -12 Associating a solution
PC-API -13 Associating an offer
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def associate_opportunity(entity_type, entity_identifier, opportunityIdentifier):
    associate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier,
        "RelatedEntityType" : entity_type,
        "RelatedEntityIdentifier" : entity_identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.associate_opportunity(**associate_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    #entity_type = Solutions | AWSProducts | AWSMarketplaceOffers
    entity_type = "Solutions"
    entity_identifier = "S-0059717"
    opportunityIdentifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Associate Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(associate_opportunity(entity_type, entity_identifier, opportunityIdentifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [AssociateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/AssociateOpportunity) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateOpportunity`
<a name="partnercentral-selling_CreateOpportunity_python_3_topic"></a>

The following code example shows how to use `CreateOpportunity`.

**SDK for Python (Boto3)**
Create an opportunity.

```
#!/usr/bin/env python
import boto3
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.helpers as helper
import utils.stringify_details as sd
from botocore.client import ClientError
from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

def create_opportunity(partner_central_client):
    create_opportunity_request = helper.remove_nulls(sd.stringify_json("src/create_opportunity/createOpportunity.json"))
    try:
        # Perform an API call
        response = partner_central_client.create_opportunity(**create_opportunity_request)

        helper.pretty_print_datetime(response)

        # Retrieve the opportunity details
        get_response = partner_central_client.get_opportunity(
            Identifier=response["Id"],
            Catalog=CATALOG_TO_USE
        )
        helper.pretty_print_datetime(get_response)
        return response
    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Create Opportunity.")
    print("-" * 88)

    partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
    )

    create_opportunity(partner_central_client)

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [CreateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateOpportunity) in *AWS SDK for Python (Boto3) API Reference*.

### `DisassociateOpportunity`
<a name="partnercentral-selling_DisassociateOpportunity_python_3_topic"></a>

The following code example shows how to use `DisassociateOpportunity`.

**SDK for Python (Boto3)**
Remove an existing association between an Opportunity and related entities.

```
#!/usr/bin/env python

"""
Purpose
PC-API -14 Removing a Solution
PC-API -15 Removing an offer
PC-API -16 Removing a product
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def disassociate_opportunity(entity_type, entity_identifier, opportunityIdentifier):
    disassociate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier,
        "RelatedEntityType" : entity_type,
        "RelatedEntityIdentifier" : entity_identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.disassociate_opportunity(**disassociate_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    #entity_type = Solutions | AWSProducts | AWSMarketplaceOffers
    entity_type = "Solutions"
    entity_identifier = "S-0049999"
    opportunityIdentifier = "O4397574"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get updated Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(disassociate_opportunity(entity_type, entity_identifier, opportunityIdentifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [DisassociateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/DisassociateOpportunity) in *AWS SDK for Python (Boto3) API Reference*.

### `GetAwsOpportunitySummary`
<a name="partnercentral-selling_GetAwsOpportunitySummary_python_3_topic"></a>

The following code example shows how to use `GetAwsOpportunitySummary`.

**SDK for Python (Boto3)**
Retrieves a summary of an AWS Opportunity.

```
#!/usr/bin/env python

"""
Purpose
PC-API-25 Retrieves a summary of an AWS Opportunity. LifeCycle.ReviewStatus=Approved
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_opportunity(identifier):
    get_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "RelatedOpportunityIdentifier": identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.get_aws_opportunity_summary(**get_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get AWS Opportunity summary.")
    print("-" * 88)

    helper.pretty_print_datetime(get_opportunity(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [GetAwsOpportunitySummary](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary) in *AWS SDK for Python (Boto3) API Reference*.

### `GetEngagementInvitation`
<a name="partnercentral-selling_GetEngagementInvitation_python_3_topic"></a>

The following code example shows how to use `GetEngagementInvitation`.

**SDK for Python (Boto3)**
Retrieves the details of an engagement invitation shared by AWS with a partner.

```
#!/usr/bin/env python

"""
Purpose
PC-API-22  GetOpportunityEngagementInvitation - Retrieves details of a specific engagement invitation.
This operation allows partners to view the invitation and its associated information,
such as the customer, project, and lifecycle details.
"""
import json
import logging
import boto3
import utils.helpers as helper

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_opportunity_engagement_invitation(identifier):
    get_opportunity_engagement_invitation_request ={
        "Catalog": CATALOG_TO_USE,
	    "Identifier": identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.get_engagement_invitation(**get_opportunity_engagement_invitation_request)
        return response

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    identifier = "arn:aws:partnercentral-selling:us-east-1:aws:catalog/Sandbox/engagement-invitation/engi-0000000IS0Qga"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Given the ARN identifier, retrieve details of Opportunity Engagement Invitation.")
    print("-" * 88)

    helper.pretty_print_datetime(get_opportunity_engagement_invitation(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [GetEngagementInvitation](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetEngagementInvitation) in *AWS SDK for Python (Boto3) API Reference*.

### `GetOpportunity`
<a name="partnercentral-selling_GetOpportunity_python_3_topic"></a>

The following code example shows how to use `GetOpportunity`.

**SDK for Python (Boto3)**
Get an opportunity.

```
#!/usr/bin/env python

"""
Purpose
PC-API -08 Get updated Opportunity given opportunity id
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_opportunity(identifier):
    get_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "Identifier": identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.get_opportunity(**get_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get updated Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(get_opportunity(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [GetOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetOpportunity) in *AWS SDK for Python (Boto3) API Reference*.

### `ListEngagementInvitations`
<a name="partnercentral-selling_ListEngagementInvitations_python_3_topic"></a>

The following code example shows how to use `ListEngagementInvitations`.

**SDK for Python (Boto3)**
Retrieves a list of engagement invitations sent to the partner.

```
#!/usr/bin/env python

"""
Purpose
PC-API-21 ListEngagementInvitations - Retrieves a list of engagement invitations based on specified criteria.
This operation allows partners to view all invitations to engagement.
"""
import json
import logging
import boto3
import utils.helpers as helper

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def list_engagement_invitations():
    list_engagement_invitations_request ={
        "Catalog": CATALOG_TO_USE,
        "MaxResults": 20
    }
    try:
        # Perform an API call
        response = partner_central_client.list_engagement_invitations(**list_engagement_invitations_request)
        return response

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Retrieve list of Engagement Invitations.")
    print("-" * 88)

    helper.pretty_print_datetime(list_engagement_invitations())

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [ListEngagementInvitations](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagementInvitations) in *AWS SDK for Python (Boto3) API Reference*.

### `ListOpportunities`
<a name="partnercentral-selling_ListOpportunities_python_3_topic"></a>

The following code example shows how to use `ListOpportunities`.

**SDK for Python (Boto3)**
List opportunities.

```
#!/usr/bin/env python

"""
Purpose
PC-API -18 Getting list of Opportunities
"""
import json
import logging
import boto3
import utils.helpers as helper

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_list_of_opportunities():

    opportunity_list = []

    list_opportunities_request ={
        "Catalog": CATALOG_TO_USE,
	    "MaxResults": 20
    }
    try:
        # Perform an API call
        response = partner_central_client.list_opportunities(**list_opportunities_request)
        opportunity_list.extend(response["OpportunitySummaries"])

        while "NextToken" in response and response["NextToken"] is not None:
            list_opportunities_request["NextToken"] = response["NextToken"]
            response = partner_central_client.list_opportunities(**list_opportunities_request)
            opportunity_list.extend(response["OpportunitySummaries"])

        return opportunity_list

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Getting list of Opportunities.")
    print("-" * 88)

    helper.pretty_print_datetime(get_list_of_opportunities())

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [ListOpportunities](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListOpportunities) in *AWS SDK for Python (Boto3) API Reference*.

### `ListSolutions`
<a name="partnercentral-selling_ListSolutions_python_3_topic"></a>

The following code example shows how to use `ListSolutions`.

**SDK for Python (Boto3)**
Retrieves a list of Partner Solutions that the partner registered on Partner Central.

```
#!/usr/bin/env python

"""
Purpose
PC-API-10 Getting list of solutions
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_list_of_solutions():
    list_solutions_request ={
        "Catalog": CATALOG_TO_USE,
	    "MaxResults": 20
    }
    try:
        # Perform an API call
        response = partner_central_client.list_solutions(**list_solutions_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Getting list of solutions.")
    print("-" * 88)

    helper.pretty_print_datetime(get_list_of_solutions())

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [ListSolutions](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListSolutions) in *AWS SDK for Python (Boto3) API Reference*.

### `RejectEngagementInvitation`
<a name="partnercentral-selling_RejectEngagementInvitation_python_3_topic"></a>

The following code example shows how to use `RejectEngagementInvitation`.

**SDK for Python (Boto3)**
Rejects an EngagementInvitation that AWS shared.

```
#!/usr/bin/env python

"""
Purpose
PC-API-05 AWS Originated AO rejection - RejectOpportunityEngagementInvitation - Rejects a engagement invitation.
This action indicates that the partner does not wish to participate in the engagement and
provides a reason for the rejection.
Upon rejection, a OpportunityEngagementInvitationRejected event is triggered.
Subsequently, the invitation will no longer be available for the partner to act on.
"""
import json
import logging
import boto3
import utils.helpers as helper

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def reject_opportunity_engagement_invitation(identifier, reject_reason):
    reject_opportunity_engagement_invitation_request ={
        "Catalog": CATALOG_TO_USE,
	    "Identifier": identifier,
        "RejectionReason": reject_reason
    }
    try:
        # Perform an API call
        response = partner_central_client.reject_engagement_invitation(**reject_opportunity_engagement_invitation_request)
        return response

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    identifier = "arn:aws:partnercentral:us-east-1::catalog/Sandbox/engagement-invitation/engi-0000002isviga"
    reject_reason = "Customer problem unclear"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Given the ARN identifier and reject reason, reject the Opportunity Engagement Invitation.")
    print("-" * 88)

    helper.pretty_print_datetime(reject_opportunity_engagement_invitation(identifier, reject_reason))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [RejectEngagementInvitation](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/RejectEngagementInvitation) in *AWS SDK for Python (Boto3) API Reference*.

### `StartEngagementByAcceptingInvitationTask`
<a name="partnercentral-selling_StartEngagementByAcceptingInvitationTask_python_3_topic"></a>

The following code example shows how to use `StartEngagementByAcceptingInvitationTask`.

**SDK for Python (Boto3)**
Starts the engagement by accepting an EngagementInvitation.

```
#!/usr/bin/env python

"""
Purpose
PC-API -11 Associating a product
PC-API -12 Associating a solution
PC-API -13 Associating an offer
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_opportunity(identifier):
    get_opportunity_request ={
	    "Identifier": identifier,
        "Catalog": CATALOG_TO_USE
    }
    try:
        # Perform an API call
        response = partner_central_client.get_engagement_invitation(**get_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def start_engagement_by_accepting_invitation_task(identifier):

    response = get_opportunity(identifier)

    if ( response['Status'] == 'PENDING') :
        accept_opportunity_engagement_invitation_request ={
            "Catalog": CATALOG_TO_USE,
	        "Identifier" : identifier,
            "ClientToken": "test-123456"
        }
        try:
            # Perform an API call
            response = partner_central_client.start_engagement_by_accepting_invitation_task(**accept_opportunity_engagement_invitation_request)
            return response

        except ClientError as err:
            # Catch all client exceptions
            print(err.response)
            return None
    else:
        return None

def usage_demo():
    identifier = "arn:aws:partnercentral:us-east-1::catalog/Sandbox/engagement-invitation/engi-0000002isusga"
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get updated Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(start_engagement_by_accepting_invitation_task(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [StartEngagementByAcceptingInvitationTask](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/StartEngagementByAcceptingInvitationTask) in *AWS SDK for Python (Boto3) API Reference*.

### `StartEngagementFromOpportunityTask`
<a name="partnercentral-selling_StartEngagementFromOpportunityTask_python_3_topic"></a>

The following code example shows how to use `StartEngagementFromOpportunityTask`.

**SDK for Python (Boto3)**
Initiates the engagement process from an existing opportunity by accepting the engagement invitation and creating a corresponding opportunity in the partner’s system.

```
#!/usr/bin/env python

"""
Purpose
PC-API -11 Associating a product
PC-API -12 Associating a solution
PC-API -13 Associating an offer
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def start_engagement_from_opportunity_task(identifier):

    start_engagement_from_opportunity_task_request ={
            "AwsSubmission": {
                "InvolvementType": "Co-Sell",
                "Visibility": "Full"
            },
            "Catalog": CATALOG_TO_USE,
	        "Identifier" : identifier,
            "ClientToken": "test-annjqwesdsd99"
    }
    try:
            # Perform an API call
            response = partner_central_client.start_engagement_from_opportunity_task(**start_engagement_from_opportunity_task_request)
            return response

    except ClientError as err:
            # Catch all client exceptions
            print(err.response)
            return None

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Start Engagement from Opportunity Task.")
    print("-" * 88)

    helper.pretty_print_datetime(start_engagement_from_opportunity_task(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [StartEngagementFromOpportunityTask](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask) in *AWS SDK for Python (Boto3) API Reference*.

### `UpdateOpportunity`
<a name="partnercentral-selling_UpdateOpportunity_python_3_topic"></a>

The following code example shows how to use `UpdateOpportunity`.

**SDK for Python (Boto3)**
Update an opportunity.

```
#!/usr/bin/env python

"""
Purpose
PC-API-2  Updating Partner Originated Opportunity
"""
import logging
import boto3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.helpers as helper
from botocore.client import ClientError
import utils.stringify_details as sd
from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_opportunity(identifier):
    get_opportunity_request ={
	    "Identifier": identifier,
        "Catalog": CATALOG_TO_USE
    }
    try:
        # Perform an API call
        response = partner_central_client.get_opportunity(**get_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def update_opportunity():
    update_opportunity_request_orig = sd.stringify_json("src/update_opportunity/update_opportunity_technical_validation.json")
    update_opportunity_request = helper.remove_nulls(update_opportunity_request_orig)

    try:
        # Perform an API call
        response = partner_central_client.update_opportunity(**update_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def update_opportunity_if_eligible(identifier):
    response = get_opportunity(identifier)
    if response is not None:
        return update_opportunity()
    else:
        print("Failed to retrieve opportunity details")

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Updating opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(update_opportunity_if_eligible(identifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [UpdateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/UpdateOpportunity) in *AWS SDK for Python (Boto3) API Reference*.

## Scenarios
<a name="scenarios"></a>

### Update associated entity of an opportunity
<a name="partnercentral-selling__UpdateAssociatedEntity_python_3_topic"></a>

The following code example shows how to:
+ Disassociate an old entity.
+ Associate a new entity.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/partner-central-api-sample-codes/python_preview/#code-examples).
Update Associated Entity of an opportunity

```
#!/usr/bin/env python

"""
Purpose
PC-API -17 Replacing a solution
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def replace_solution(original_entity_identifier, new_entity_identifier, opportunityIdentifier):
    disassociate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier,
        "RelatedEntityType" : "Solutions",
        "RelatedEntityIdentifier" : original_entity_identifier
    }

    associate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier,
        "RelatedEntityType" : "Solutions",
        "RelatedEntityIdentifier" : new_entity_identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.disassociate_opportunity(**disassociate_opportunity_request)
        response = partner_central_client.associate_opportunity(**associate_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    original_entity_identifier = "S-0049999"
    new_entity_identifier = "S-0050014"
    opportunityIdentifier = "O4397574"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Replacing a solution.")
    print("-" * 88)

    helper.pretty_print_datetime(replace_solution(original_entity_identifier, new_entity_identifier, opportunityIdentifier))

if __name__ == "__main__":
    usage_demo()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [AssociateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/AssociateOpportunity)
  + [DisassociateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/DisassociateOpportunity)
