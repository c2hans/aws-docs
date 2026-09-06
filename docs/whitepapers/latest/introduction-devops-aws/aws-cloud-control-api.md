---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cloud-control-api.html
---

# AWS Cloud Control API
<a name="aws-cloud-control-api"></a>

 [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi/) is a new AWS capability that introduces a common set of Create, Read, Update, Delete, and List (CRUDL) APIs to help developers manage their cloud infrastructure in an easy and consistent way. The Cloud Control API common APIs allow developers to uniformly manage the lifecycle of AWS and third-party services.

 As a developer, you might prefer to simplify the way you manage the lifecycle of all your resources. You can use Cloud Control API's uniform resource configuration model with a pre-defined format to standardize your cloud resource configuration. In addition, you will benefit from uniform API behavior (response elements and errors) while managing your resources.

 For example, you will find it simple to debug errors during CRUDL operations through uniform error codes surfaced by Cloud Control API that are independent of the resources you operate on. Using Cloud Control API, you will also find it simple to configure cross-resource dependencies. You will also no longer require to author and maintain custom code across multiple vendor tools and APIs to use AWS and third-party resources together.
