---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/acl.html
---

# Anti-corruption layer pattern
<a name="acl"></a>

## Intent
<a name="acl-intent"></a>

The anti-corruption layer (ACL) pattern acts as a mediation layer that translates domain model semantics from one system to another system. It translates the model of the upstream bounded context (monolith) into a model that suits the downstream bounded context (microservice) before consuming the communication contract that's established by the upstream team. This pattern might be applicable when the downstream bounded context contains a core subdomain, or the upstream model is an unmodifiable legacy system. It also reduces transformation risk and business disruption by preventing changes to callers when their calls have to be redirected transparently to the target system.

## Motivation
<a name="acl-motivation"></a>

During the migration process, when a monolithic application is migrated into microservices, there might be changes in the domain model semantics of the newly migrated service. When the features within the monolith are required to call these microservices, the calls should be routed to the migrated service without requiring any changes to the calling services. The ACL pattern allows the monolith to call the microservices transparently by acting as an adapter or a facade layer that translates the calls into the newer semantics.

## Applicability
<a name="acl-applicability"></a>

Consider using this pattern when:
+ Your existing monolithic application has to communicate with a function that has been migrated into a microservice, and the migrated service domain model and semantics differ from the original feature.
+ Two systems have different semantics and need to exchange data, but it isn't practical to modify one system to be compatible with the other system.
+ You want to use a quick and simplified approach to adapt one system to another with minimal impact.
+ Your application is communicating with an external system.

## Issues and considerations
<a name="acl-issues"></a>
+ **Team dependencies:** When different services in a system are owned by different teams, the new domain model semantics in the migrated services can lead to changes in the calling systems. However, teams might not be able to make these changes in a coordinated way, because they might have other  priorities. ACL decouples the callees and translates the calls to match the semantics of the new services, thus avoiding the need for callers to make changes in the current system.
+ **Operational overhead:** The ACL pattern requires additional effort to operate and maintain. This work includes integrating ACL with monitoring and alerting tools, the release process, and continuous integration and continuous delivery (CI/CD) processes.
+ **Single point of failure:** Any failures in the ACL can make the target service unreachable, causing application issues. To mitigate this issue, you should build in retry capabilities and circuit breakers. See the [retry with backoff](retry-backoff.md) and [circuit breaker](circuit-breaker.md) patterns to understand more about these options. Setting up appropriate alerts and logging will improve the mean time to resolution (MTTR).
+ **Technical debt:** As part of your migration or modernization strategy, consider whether the ACL will be a transient or interim solution, or a long-term solution. If it's an interim solution, you should record the ACL as a technical debt and decommission it after all dependent callers have been migrated.
+ **Latency:** The additional layer can introduce latency due to the conversion of requests from one interface to another. We recommend that you define and test performance tolerance in applications that are sensitive to response time before you deploy ACL into production environments.
+ **Scaling bottleneck:** In high-load applications where services can scale to peak load, ACL can become a bottleneck and might cause scaling issues. If the target service scales on demand, you should design ACL to scale accordingly.
+ **Service-specific or shared implementation:** You can design ACL as a shared object to convert and redirect calls to multiple services or service-specific classes. Take latency, scaling, and failure tolerance into account when you determine the implementation type for ACL.

## Implementation
<a name="acl-implementation"></a>

You can implement ACL inside your monolithic application as a class that's specific to the service that's being migrated, or as an independent service. The ACL must be decommissioned after all dependent services have been migrated into the microservices architecture.

### High-level architecture
<a name="high-level-architecture.6a4e8098-b5a5-5cea-9b11-f82a881f76d3"></a>

In the following example architecture, a monolithic application has three services: user service, cart service, and account service. The cart service is dependent on the user service, and the application uses a monolithic relational database.

![Monolithic application with three services](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/96c5b594-d1bb-4a54-8cc2-d9d088490039.png)

In the following architecture, the user service has been migrated to a new microservice. The cart service calls the user service, but the implementation is no longer available within the monolith.  It's also likely that the interface of the newly migrated service won't match its previous interface, when it was inside the monolithic application.

![Monolithic application where one service is moved out to a microservice](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/d37cfd9a-8938-40d4-bcd3-4f37154c5cb9.png)

If the cart service has to call the newly migrated user service directly, this will require changes to the cart service and a thorough testing of the monolithic application. This can increase the transformation risk and business disruption. The goal should be to minimize the changes to the existing functionality of the monolithic application.

In this case, we recommend that you introduce an ACL between the old user service and the newly migrated user service. The ACL works as an adapter or a facade that converts the calls into the newer interface. ACL can be implemented inside the monolithic application as a class (for example, `UserServiceFacade` or `UserServiceAdapter`) that's specific to the service that was migrated. The anti-corruption layer must be decommissioned after all dependent services have been migrated into the microservices architecture.

![Adding an anti-corruption layer](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/d06ebf02-c3b5-4224-b091-dc8d0026c0a9.png)

### Implementation using AWS services
<a name="implementation-using-aws-services.ee35f591-9b60-5188-b84a-ca0e89b92603"></a>

The following diagram shows how you can implement this ACL example by using AWS services.

![Implementing the ACL pattern with AWS services.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/d0b414ab-9b41-46a8-949d-44289eac047d.png)

The user microservice is migrated out of the ASP.NET monolithic application and deployed as an [AWS Lambda](https://aws.amazon.com/lambda/) function on AWS. Calls to the Lambda function are routed through [Amazon API Gateway](https://aws.amazon.com/api-gateway/). ACL is deployed in the monolith to translate the call to adapt to the semantics of the user microservice.

When `Program.cs` calls the user service (`UserInMonolith.cs`) inside the monolith, the call is routed to the ACL (`UserServiceACL.cs`). The ACL translates the call to the new semantics and interface, and calls the microservice through the API Gateway endpoint. The caller (`Program.cs`) isn't aware of the translation and routing that take place in the user service and ACL. Because the caller isn't aware of the code changes, there is less business disruption and reduced transformation risk.

### Sample code
<a name="sample-code.9a75c9a1-77c3-5ea7-82db-d2999b0e02b1"></a>

The following code snippet provides the changes to the original service and the implementation of `UserServiceACL.cs`. When a request is received, the original user service calls the ACL. The ACL converts the source object to match the interface of the newly migrated service, calls the service, and returns the response to the caller.

```
public class UserInMonolith: IUserInMonolith
{
    private readonly IACL _userServiceACL;
    public UserInMonolith(IACL userServiceACL) => (_userServiceACL) = (userServiceACL);
    public async Task<HttpStatusCode> UpdateAddress(UserDetails userDetails)
    {
        //Wrap the original object in the derived class
        var destUserDetails = new UserDetailsWrapped("user", userDetails);
        //Logic for updating address has been moved to a microservice
        return await _userServiceACL.CallMicroservice(destUserDetails);
    }
}

public class UserServiceACL: IACL
{
    static HttpClient _client = new HttpClient();
    private static string _apiGatewayDev = string.Empty;

    public UserServiceACL()
    {
        IConfiguration config = new ConfigurationBuilder().AddJsonFile(AppContext.BaseDirectory + "../../../config.json").Build();
        _apiGatewayDev = config["APIGatewayURL:Dev"];
        _client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
    }
    public async Task<HttpStatusCode> CallMicroservice(ISourceObject details)
    {
        _apiGatewayDev +=  "/" + details.ServiceName;
        Console.WriteLine(_apiGatewayDev);

        var userDetails = details as UserDetails;
        var userMicroserviceModel = new UserMicroserviceModel();
        userMicroserviceModel.UserId = userDetails.UserId;
        userMicroserviceModel.Address = userDetails.AddressLine1 + ", " + userDetails.AddressLine2;
        userMicroserviceModel.City = userDetails.City;
        userMicroserviceModel.State = userDetails.State;
        userMicroserviceModel.Country = userDetails.Country;

        if (Int32.TryParse(userDetails.ZipCode, out int zipCode))
        {
            userMicroserviceModel.ZipCode = zipCode;
            Console.WriteLine("Updated zip code");
        }
        else
        {
            Console.WriteLine("String could not be parsed.");
            return HttpStatusCode.BadRequest;
        }

        var jsonString = JsonSerializer.Serialize<UserMicroserviceModel>(userMicroserviceModel);
        var payload = JsonSerializer.Serialize(userMicroserviceModel);
        var content = new StringContent(payload, Encoding.UTF8, "application/json");

        var response = await _client.PostAsync(_apiGatewayDev, content);
        return response.StatusCode;
    }
}
```

### GitHub repository
<a name="github-repository.1b7f74c7-1a8e-50a9-98db-215b7bc417b0"></a>

For a complete implementation of the sample architecture for this pattern, see the GitHub repository at [https://github.com/aws-samples/anti-corruption-layer-pattern](https://github.com/aws-samples/anti-corruption-layer-pattern).

## Related content
<a name="acl-resources"></a>
+ [Strangler fig pattern](strangler-fig.md)
+ [Circuit breaker pattern](circuit-breaker.md)
+ [Retry with backoff pattern](retry-backoff.md)
