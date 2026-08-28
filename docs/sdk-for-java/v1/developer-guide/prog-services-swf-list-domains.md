---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/prog-services-swf-list-domains.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# Listing Domains
<a name="prog-services-swf-list-domains"></a>

You can list the [Amazon SWF](https://aws.amazon.com/swf/) domains associated with your account and AWS region by registration type.

1. Create a [ListDomainsRequest](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/ListDomainsRequest.html) object, and specify the registration status of the domains that you’re interested in—​this is required.

1. Call [AmazonSimpleWorkflowClient.listDomains](http://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/AmazonSimpleWorkflowClient.html#listDomains-com.amazonaws.services.simpleworkflow.model.ListDomainsRequest-) with the *ListDomainRequest* object. Results are provided in a [DomainInfos](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/DomainInfos.html) object.

1. Call [getDomainInfos](http://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/DomainInfos.html#getDomainInfos--) on the returned object to get a list of [DomainInfo](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/DomainInfo.html) objects.

1. Call [getName](http://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/services/simpleworkflow/model/DomainInfo.html#getName--) on each *DomainInfo* object to get its name.

The following code demonstrates this procedure:

```
public void list_swf_domains(AmazonSimpleWorkflowClient swf)
{
    ListDomainsRequest request = new ListDomainsRequest();
    request.setRegistrationStatus("REGISTERED");
    DomainInfos domains = swf.listDomains(request);
    System.out.println("Current Domains:");
    for (DomainInfo di : domains.getDomainInfos())
    {
        System.out.println(" * " + di.getName());
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
