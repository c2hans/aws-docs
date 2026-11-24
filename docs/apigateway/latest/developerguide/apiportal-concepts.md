---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-concepts.html
---

# API Portal concepts

The following terms describe the objects that API Portal works with.

*API inventory*
The continuously updated list of every API that discovery has found in your account or organization. Each row is one API: an HTTP method and path on a front-door resource, with its host, source service, owning account, visibility, AWS WAF status, and classification.

*Discovery configuration*
The settings that control discovery in one account and Region, or across an organization in one Region: which services to scan, which resources, accounts, or organizational units to exclude, and whether AI endpoint identification is on. An organization discovery configuration belongs to the management account.

*Discovered API*
Any API in the inventory. A discovered API is identified by its method, host, port, path, and the Amazon Resource Name (ARN) of the API Gateway, Application Load Balancer, or CloudFront resource that serves it.

*Shadow API*
A discovered API that no account in your organization has promoted to a managed API. Every discovered API starts as a shadow API. A shadow API exists and is reachable, but it isn't governed.

*Managed API*
A discovered API that you promoted. Managed APIs are evaluated for security posture and are the only APIs that you can add to a product and publish in a documentation portal. Promoting an API doesn't change the underlying resource. You can remove an API from managed APIs to return it to shadow. When you do, API Portal stops evaluating its security posture, removes it from any products that include it (the change takes effect in a documentation portal the next time you publish), and no longer counts it as a documented API.

*Zombie API*
A managed API that has received no traffic for 30 days and whose backing resource has had no configuration change for 90 days. Both conditions must be true. The API is still reachable, so the label clears when traffic resumes.

*Orphaned API*
A managed API whose owning account has left your organization or been closed. The inventory keeps a last-known snapshot of the API, but it's no longer rediscovered and its findings are no longer updated. Moving an account between organizational units doesn't make its APIs orphaned. If an API is both zombie and orphaned, API Portal shows it as orphaned.

*AI workload*
An AI protocol seen in an API's traffic when AI endpoint identification is enabled: MCP (Model Context Protocol), A2A (Agent2Agent protocol), or LLM (traffic to or from a large language model (LLM) inference server or gateway).

*Product*
A named group of managed APIs together with its documentation. A product has an overview page, an API reference page for each API (a *product API page*), any custom pages that you create (*product pages*), and optionally a *sharing policy* that lets other accounts publish it. Consumers browse a documentation portal by product.

*Documentation portal*
The branded website that your API consumers visit. A documentation portal contains one or more products. When you publish a documentation portal, API Portal captures the current state of its products and pages and serves that snapshot until you publish again.
