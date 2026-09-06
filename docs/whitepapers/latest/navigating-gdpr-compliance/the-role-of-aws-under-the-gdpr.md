---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/the-role-of-aws-under-the-gdpr.html
---

# The Role of AWS Under the GDPR
<a name="the-role-of-aws-under-the-gdpr"></a>

Under the GDPR, AWS may act as either a processor or a controller, depending on the service and how it is used. A controller is the entity that decides why and how personal data is processed. A processor handles personal data only on the controller's behalf and only for the purposes the controller defines. This distinction matters because it determines whether AWS or the customer is responsible for decisions about how personal data is handled and which party is accountable for meeting specific GDPR obligations.

The AWS DPA applies specifically to customer data uploaded and managed by the customer through AWS services.

## AWS as a Processor
<a name="aws-as-a-processor"></a>

When AWS customers use AWS services to process customer data in their content, AWS acts as a processor. Customers typically remain as controller and determine the purposes and means of processing. For example, customers can use the controls available in AWS services, including security configuration controls, to process customer data. The [AWS DPA](https://d1.awsstatic.com/legal/aws-dpa/aws-dpa.pdf) incorporates AWS's commitments as processor or sub-processor.

## AWS as a Controller
<a name="aws-as-a-controller"></a>

When AWS collects customer data and determines the purposes and means of processing (e.g., for account registration, administration or customer support), it acts as a controller. The [AWS Privacy Notice](https://aws.amazon.com/privacy/) describes how AWS collects, uses and discloses customer data where it acts as controller.

## AWS metadata processing
<a name="aws-metadata-processing"></a>

AWS acts as a controller for operational metadata it generates or collects to operate services, manage accounts, bill customers and maintain security (such as account IDs, billing information, and security logs). AWS processes such metadata as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

For metadata customers generate or configure through AWS services (customer-created metadata), AWS does not act as processor, since AWS retains control over processing locations and determines other related processing aspects for this metadata.
