---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains-consumer-delete-domain-name-access-association.html
---

# API consumer: Delete your domain name access association with a private custom domain name
<a name="apigateway-private-custom-domains-consumer-delete-domain-name-access-association"></a>

If you are an API consumer, at any time, you can delete the access association resource. The API provider can't delete the domain name access association for you.

We recommend that you always delete a domain name access association when you're no longer using it.

------
#### [ AWS Management Console ]

**To delete the domain name access association**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, choose **Domain name access associations**.

1. Select your domain name access association, and then choose **Delete**.

1. Confirm your choice, and then choose **Delete**.

------
#### [ AWS CLI ]

The following `delete-access-association` command deletes the access association:

```
aws apigateway delete-domain-name-access-association \
    --domain-name-access-association-arn 'arn:aws:apigateway:us-west-2:444455556666:/domainnameaccessassociations/domainname/private.example.com+abcd1234/vpcesource/vpce-abcd1234efg'
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
