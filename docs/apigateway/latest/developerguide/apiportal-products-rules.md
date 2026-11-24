---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-products-rules.html
---

# Create a rule-based product in API Portal

A rule-based product's membership is derived from rules that you write. Every managed API in your account that matches is in the product, and an API that stops matching is removed. You don't add or remove APIs by hand. Use rule-based products for groupings that follow a convention, such as every API on one host or every API owned by one account.

## How rules are evaluated
<a name="apiportal-products-rules-how"></a>

A rule is a filter on one attribute of the managed API's signature, with up to 10 values. A product can have one filter per attribute, up to six. Filters are combined with AND; the values within one filter are combined with OR. Values match exactly and are case-sensitive; wildcards aren't supported.

| Attribute | Matches |
| --- | --- |
| Resource ARN | The ARN of the API Gateway, Application Load Balancer, or CloudFront resource that serves the API. |
| Host | The hostname, for example orders.example.com. |
| Method | The HTTP method name, for example GET. |
| Path | The path, for example /v1/orders. |
| Port | The port as a number, for example 443. |
| Account | The account that hosts the API. For a managed API created at organization scope, this is the member account, not the account that promoted it. |

After you create or update a rule-based product, its status is **In progress** while membership is evaluated, then **Active**. If an API that stopped matching still has an API reference page, it stays in the product and the status shows **Failed** with the reason; delete the page and update the product to retry.

## Create a rule-based product
<a name="apiportal-products-rules-create"></a>

**To create a rule-based product**

1. Under **API Portal**, choose **Products**, and then **Create product**.

1. Enter a name and, optionally, a description.

1. For **Product type**, choose **Rule-based**.

1. Under **Rules**, choose an attribute, enter one or more values, and choose **Add rule**. Repeat for each attribute you want to filter on. The page shows the managed APIs that currently match.

1. Choose **Next**, review, and choose **Create product**.

To change the rules later, choose **Edit** on the product detail page. The rules are replaced as a whole, not merged.

Using the AWS CLI, this product includes every managed API on one host whose method is `GET` or `POST`:

```
aws apiportal create-product \
    --display-name "Orders service" \
    --api-selection-configuration '{"apiSelectionMode":"RULE_BASED","ruleFilters":[{"key":"HOST","values":["orders.example.com"]},{"key":"METHOD","values":["GET","POST"]}]}' \
    --region us-east-1
```
