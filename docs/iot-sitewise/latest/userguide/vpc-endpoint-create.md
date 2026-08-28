---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vpc-endpoint-create.html
---

# Create an interface VPC endpoint for AWS IoT SiteWise
<a name="vpc-endpoint-create"></a>

To create a VPC endpoint for the AWS IoT SiteWise service, use either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for AWS IoT SiteWise by using one of the following service names:
+ For the **data plane** API operations, use the following service name:

  ```
  com.amazonaws.{{region}}.iotsitewise.data
  ```
+ For the **control plane** API operations, use the following service name:

  ```
  com.amazonaws.{{region}}.iotsitewise.api
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
