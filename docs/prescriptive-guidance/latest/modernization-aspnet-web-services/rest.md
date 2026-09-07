---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/rest.html
---

# REST-based ASP.NET web services
<a name="rest"></a>

When you modernize REST-based ASP.NET services on AWS by using the strangler fig pattern, we recommend that you use Amazon API Gateway to establish the proxy that will be used to divert traffic to the new service. You can introduce an API Gateway endpoint as the intermediary between service consumers and the legacy service that is being modernized. If the legacy service is already on AWS, the API Gateway endpoint is configured to route requests to the legacy REST service. If the service is not yet on AWS, it can be migrated as is before establishing the new API Gateway proxy. If that isn't possible, you can take a hybrid cloud approach by using an AWS connectivity service such as AWS Direct Connect to connect API Gateway to your on-premises data center. The following illustration depicts the ASP.NET REST service and its consumer before and after the introduction of API Gateway as a proxy between the two.

Before the introduction of a proxy:

![REST service and its consumer before the introduction of a proxy between the two.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/4ba2047e-afdb-4ccf-a595-cac64f9d19bd.png)

After adding API Gateway as a proxy:

![REST service and its consumer with API Gateway added as a proxy between the two.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/f41763bd-afa2-4f6d-aacf-3885a49e3511.png)

When the API Gateway proxy is in place, you can create and deploy the modernized service on AWS by using Amazon ECS, for example, to achieve a highly scalable and available service. When the proxy and newly modernized service have been created and tested, you can reconfigure the API Gateway endpoint to point to the modernized REST API for its implementation.

![REST service and its consumer with API Gateway reconfigured to point to the modernized REST API.](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/images/guide-img/5e1df9e0-2643-4e7a-8b08-fc2f99f03ade/images/7c09c7bb-8213-4267-ab61-b5d65550bdc4.png)

If the newly modernized service has an API contract that is different from the legacy proxy contract the consuming systems depend on, you can use the API Gateway data transformation feature. Incoming API requests that are structured using the legacy system's schema can be mapped and transformed to the new service's contract.
