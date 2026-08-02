---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/operations.html
---

# Operations
<a name="operations"></a>

The Amazon API Gateway REST API includes the following operations.
+ [CreateApi](apis.md#CreateApi)

  Creates an `Api` resource.
+ [CreateApiMapping](domainnames-domainname-apimappings.md#CreateApiMapping)

  Creates an API mapping.
+ [CreateAuthorizer](apis-apiid-authorizers.md#CreateAuthorizer)

  Creates an `Authorizer` for an API.
+ [CreateDeployment](apis-apiid-deployments.md#CreateDeployment)

  Creates a `Deployment` for an API.
+ [CreateDomainName](domainnames.md#CreateDomainName)

  Creates a domain name.
+ [CreateIntegration](apis-apiid-integrations.md#CreateIntegration)

  Creates an `Integration`.
+ [CreateIntegrationResponse](apis-apiid-integrations-integrationid-integrationresponses.md#CreateIntegrationResponse)

  Creates an `IntegrationResponses`.
+ [CreateModel](apis-apiid-models.md#CreateModel)

  Creates a `Model` for an API.
+ [CreatePortal](portals.md#CreatePortal)

  Creates a portal.
+ [CreatePortalProduct](portalproducts.md#CreatePortalProduct)

  Creates a new portal product.
+ [CreateProductPage](portalproducts-portalproductid-productpages.md#CreateProductPage)

  Creates a new product page for a portal product.
+ [CreateProductRestEndpointPage](portalproducts-portalproductid-productrestendpointpages.md#CreateProductRestEndpointPage)

  Creates a product REST endpoint page for a portal product.
+ [CreateRoute](apis-apiid-routes.md#CreateRoute)

  Creates a `Route` for an API.
+ [CreateRouteResponse](apis-apiid-routes-routeid-routeresponses.md#CreateRouteResponse)

  Creates a `RouteResponse` for a `Route`.
+ [CreateRoutingRule](domainnames-domainname-routingrules.md#CreateRoutingRule)

  Create a routing rule.
+ [CreateStage](apis-apiid-stages.md#CreateStage)

  Creates a `Stage` for an API.
+ [CreateVpcLink](vpclinks.md#CreateVpcLink)

  Creates a VPC link.
+ [DeleteAccessLogSettings](apis-apiid-stages-stagename-accesslogsettings.md#DeleteAccessLogSettings)

  Deletes the `AccessLogSettings` for a `Stage`. To disable access logging for a `Stage`, delete its `AccessLogSettings`.
+ [DeleteApi](apis-apiid.md#DeleteApi)

  Deletes an `Api` resource.
+ [DeleteApiMapping](domainnames-domainname-apimappings-apimappingid.md#DeleteApiMapping)

  Deletes an API mapping.
+ [DeleteAuthorizer](apis-apiid-authorizers-authorizerid.md#DeleteAuthorizer)

  Deletes an `Authorizer`.
+ [DeleteCorsConfiguration](apis-apiid-cors.md#DeleteCorsConfiguration)

  Deletes a CORS configuration.
+ [DeleteDeployment](apis-apiid-deployments-deploymentid.md#DeleteDeployment)

  Deletes a `Deployment`.
+ [DeleteDomainName](domainnames-domainname.md#DeleteDomainName)

  Deletes a domain name.
+ [DeleteIntegration](apis-apiid-integrations-integrationid.md#DeleteIntegration)

  Deletes an `Integration`.
+ [DeleteIntegrationResponse](apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid.md#DeleteIntegrationResponse)

  Deletes an `IntegrationResponses`.
+ [DeleteModel](apis-apiid-models-modelid.md#DeleteModel)

  Deletes a `Model`.
+ [DeletePortal](portals-portalid.md#DeletePortal)

  Deletes a portal.
+ [DeletePortalProduct](portalproducts-portalproductid.md#DeletePortalProduct)

  Deletes a portal product.
+ [DeletePortalProductSharingPolicy](portalproducts-portalproductid-sharingpolicy.md#DeletePortalProductSharingPolicy)

  Deletes the sharing policy for a portal product.
+ [DeleteProductPage](portalproducts-portalproductid-productpages-productpageid.md#DeleteProductPage)

  Deletes a product page of a portal product.
+ [DeleteProductRestEndpointPage](portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.md#DeleteProductRestEndpointPage)

  Deletes a product REST endpoint page.
+ [DeleteRoute](apis-apiid-routes-routeid.md#DeleteRoute)

  Deletes a `Route`.
+ [DeleteRouteRequestParameter](apis-apiid-routes-routeid-requestparameters-requestparameterkey.md#DeleteRouteRequestParameter)

  Deletes a route request parameter. Supported only for WebSocket APIs.
+ [DeleteRouteResponse](apis-apiid-routes-routeid-routeresponses-routeresponseid.md#DeleteRouteResponse)

  Deletes a `RouteResponse`.
+ [DeleteRouteSettings](apis-apiid-stages-stagename-routesettings-routekey.md#DeleteRouteSettings)

  Deletes the `RouteSettings` for a stage.
+ [DeleteRoutingRule](domainnames-domainname-routingrules-routingruleid.md#DeleteRoutingRule)

  Deletes a routing rule.
+ [DeleteStage](apis-apiid-stages-stagename.md#DeleteStage)

  Deletes a `Stage`.
+ [DeleteVpcLink](vpclinks-vpclinkid.md#DeleteVpcLink)

  Deletes a VPC link.
+ [DisablePortal](portals-portalid-publish.md#DisablePortal)

  Deletes the publication of a portal portal.
+ [ExportApi](apis-apiid-exports-specification.md#ExportApi)

  Exports a definition of an API in a particular output format and specification.
+ [GetApi](apis-apiid.md#GetApi)

  Gets an `Api` resource.
+ [GetApiMapping](domainnames-domainname-apimappings-apimappingid.md#GetApiMapping)

  Gets an API mapping.
+ [GetApiMappings](domainnames-domainname-apimappings.md#GetApiMappings)

  Gets API mappings.
+ [GetApis](apis.md#GetApis)

  Gets a collection of `Api` resources.
+ [GetAuthorizer](apis-apiid-authorizers-authorizerid.md#GetAuthorizer)

  Gets an `Authorizer`.
+ [GetAuthorizers](apis-apiid-authorizers.md#GetAuthorizers)

  Gets the `Authorizers` for an API.
+ [GetDeployment](apis-apiid-deployments-deploymentid.md#GetDeployment)

  Gets a `Deployment`.
+ [GetDeployments](apis-apiid-deployments.md#GetDeployments)

  Gets the `Deployments` for an API.
+ [GetDomainName](domainnames-domainname.md#GetDomainName)

  Gets a domain name.
+ [GetDomainNames](domainnames.md#GetDomainNames)

  Gets the domain names for an AWS account.
+ [GetIntegration](apis-apiid-integrations-integrationid.md#GetIntegration)

  Gets an `Integration`.
+ [GetIntegrationResponse](apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid.md#GetIntegrationResponse)

  Gets an `IntegrationResponses`.
+ [GetIntegrationResponses](apis-apiid-integrations-integrationid-integrationresponses.md#GetIntegrationResponses)

  Gets the `IntegrationResponses` for an `Integration`.
+ [GetIntegrations](apis-apiid-integrations.md#GetIntegrations)

  Gets the `Integrations` for an API.
+ [GetModel](apis-apiid-models-modelid.md#GetModel)

  Gets a `Model`.
+ [GetModels](apis-apiid-models.md#GetModels)

  Gets the `Models` for an API.
+ [GetModelTemplate](apis-apiid-models-modelid-template.md#GetModelTemplate)

  Gets a model template.
+ [GetPortal](portals-portalid.md#GetPortal)

  Gets a portal.
+ [GetPortalProduct](portalproducts-portalproductid.md#GetPortalProduct)

  Gets a portal product.
+ [GetPortalProductSharingPolicy](portalproducts-portalproductid-sharingpolicy.md#GetPortalProductSharingPolicy)

  Gets the sharing policy for a portal product.
+ [GetProductPage](portalproducts-portalproductid-productpages-productpageid.md#GetProductPage)

  Gets a product page of a portal product.
+ [GetProductRestEndpointPage](portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.md#GetProductRestEndpointPage)

  Gets a product REST endpoint page.
+ [GetRoute](apis-apiid-routes-routeid.md#GetRoute)

  Gets a `Route`.
+ [GetRouteResponse](apis-apiid-routes-routeid-routeresponses-routeresponseid.md#GetRouteResponse)

  Gets a `RouteResponse`.
+ [GetRouteResponses](apis-apiid-routes-routeid-routeresponses.md#GetRouteResponses)

  Gets the `RouteResponses` for a `Route`.
+ [GetRoutes](apis-apiid-routes.md#GetRoutes)

  Gets the `Routes` for an API.
+ [GetRoutingRule](domainnames-domainname-routingrules-routingruleid.md#GetRoutingRule)

  Gets a routing rule.
+ [GetStage](apis-apiid-stages-stagename.md#GetStage)

  Gets a `Stage`.
+ [GetStages](apis-apiid-stages.md#GetStages)

  Gets the `Stages` for an API.
+ [GetTags](tags-resource-arn.md#GetTags)

  Gets a collection of `Tag` resources.
+ [GetVpcLink](vpclinks-vpclinkid.md#GetVpcLink)

  Gets a VPC link.
+ [GetVpcLinks](vpclinks.md#GetVpcLinks)

  Gets a collection of VPC links.
+ [ImportApi](apis.md#ImportApi)

  Imports an API.
+ [ListPortalProducts](portalproducts.md#ListPortalProducts)

  Lists portal products.
+ [ListPortals](portals.md#ListPortals)

  Lists portals.
+ [ListProductPages](portalproducts-portalproductid-productpages.md#ListProductPages)

  Lists the product pages for a portal product.
+ [ListProductRestEndpointPages](portalproducts-portalproductid-productrestendpointpages.md#ListProductRestEndpointPages)

  Lists the product REST endpoint pages of a portal product.
+ [ListRoutingRules](domainnames-domainname-routingrules.md#ListRoutingRules)

  Lists routing rules.
+ [PreviewPortal](portals-portalid-preview.md#PreviewPortal)

  Creates a portal preview.
+ [PublishPortal](portals-portalid-publish.md#PublishPortal)

  Publishes a portal.
+ [PutPortalProductSharingPolicy](portalproducts-portalproductid-sharingpolicy.md#PutPortalProductSharingPolicy)

  Updates the sharing policy for a portal product.
+ [PutRoutingRule](domainnames-domainname-routingrules-routingruleid.md#PutRoutingRule)

  Replaces an existing routing rule. When you replace an existing routing rule, the `RoutingRuleId` isn't changed.
+ [ReimportApi](apis-apiid.md#ReimportApi)

  Puts an `Api` resource.
+ [ResetAuthorizersCache](apis-apiid-stages-stagename-cache-authorizers.md#ResetAuthorizersCache)

  Resets all authorizer cache entries for the specified stage. Supported only for HTTP API Lambda authorizers.
+ [TagResource](tags-resource-arn.md#TagResource)

  Creates a new `Tag` resource to represent a tag.
+ [UntagResource](tags-resource-arn.md#UntagResource)

  Deletes a `Tag`.
+ [UpdateApi](apis-apiid.md#UpdateApi)

  Updates an `Api` resource.
+ [UpdateApiMapping](domainnames-domainname-apimappings-apimappingid.md#UpdateApiMapping)

  The API mapping.
+ [UpdateAuthorizer](apis-apiid-authorizers-authorizerid.md#UpdateAuthorizer)

  Updates an `Authorizer`.
+ [UpdateDeployment](apis-apiid-deployments-deploymentid.md#UpdateDeployment)

  Updates a `Deployment`.
+ [UpdateDomainName](domainnames-domainname.md#UpdateDomainName)

  Updates a domain name.
+ [UpdateIntegration](apis-apiid-integrations-integrationid.md#UpdateIntegration)

  Updates an `Integration`.
+ [UpdateIntegrationResponse](apis-apiid-integrations-integrationid-integrationresponses-integrationresponseid.md#UpdateIntegrationResponse)

  Updates an `IntegrationResponses`.
+ [UpdateModel](apis-apiid-models-modelid.md#UpdateModel)

  Updates a `Model`.
+ [UpdatePortal](portals-portalid.md#UpdatePortal)

  Updates a portal.
+ [UpdatePortalProduct](portalproducts-portalproductid.md#UpdatePortalProduct)

  Updates the portal product.
+ [UpdateProductPage](portalproducts-portalproductid-productpages-productpageid.md#UpdateProductPage)

  Updates a product page of a portal product.
+ [UpdateProductRestEndpointPage](portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.md#UpdateProductRestEndpointPage)

  Updates a product REST endpoint page.
+ [UpdateRoute](apis-apiid-routes-routeid.md#UpdateRoute)

  Updates a `Route`.
+ [UpdateRouteResponse](apis-apiid-routes-routeid-routeresponses-routeresponseid.md#UpdateRouteResponse)

  Updates a `RouteResponse`.
+ [UpdateStage](apis-apiid-stages-stagename.md#UpdateStage)

  Updates a `Stage`.
+ [UpdateVpcLink](vpclinks-vpclinkid.md#UpdateVpcLink)

  Updates a VPC link.
