---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services-swf-register-domain.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# Registering Domains
<a name="prog-services-swf-register-domain"></a>

Every workflow and activity in [Amazon SWF](https://aws.amazon.com/swf/) needs a *domain* to run in.

1. Create a new [RegisterDomainRequest](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/RegisterDomainRequest.html) object, providing it with at least the domain name and workflow execution retention period (these parameters are both required).

1. Call the [AmazonSimpleWorkflowClient.registerDomain](http://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.html#registerDomain-com.amazonaws.services.simpleworkflow.model.RegisterDomainRequest-) method with the *RegisterDomainRequest* object.

1. Catch the [DomainAlreadyExistsException](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/DomainAlreadyExistsException.html) if the domain you’re requesting already exists (in which case, no action is usually required).

The following code demonstrates this procedure:

```
public void register_swf_domain(AmazonSimpleWorkflowClient swf, String name)
{
    RegisterDomainRequest request = new RegisterDomainRequest().withName(name);
    request.setWorkflowExecutionRetentionPeriodInDays("10");
    try
    {
        swf.registerDomain(request);
    }
    catch (DomainAlreadyExistsException e)
    {
        System.out.println("Domain already exists!");
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
