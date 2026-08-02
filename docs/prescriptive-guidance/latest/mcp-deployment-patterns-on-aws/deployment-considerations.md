---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/deployment-considerations.html
---

# Deployment Considerations
<a name="deployment-considerations"></a>

Selecting the appropriate deployment pattern depends on your specific requirements, operational capabilities, and workload characteristics. Refer to the following decision matrix for different patterns:

|  |  |  |  |  |  |
| --- |--- |--- |--- |--- |--- |
| Consideration | Amazon Bedrock AgentCore | Lambda \+ API Gateway | ECS | EKS | EC2 |
| Best For | Production MCP, AWS-native | Variable traffic, event-driven | Containerized apps, moderate scale | Complex microservices, multi-tenant | Persistent connections, full control |
| Management Overhead | Minimal | Minimal | Medium | Very High | High |
| Complexity | Low | Low | Medium | High | Medium |
| Scaling | Automatic | Automatic  | Automatic | Automatic (advanced) | Manual/ASG |
| Cost (low traffic) | Low | Low | Medium | Highest | Medium |
| Cost (high traffic) | Low | Medium | Medium | Medium | Lowest |
| Cold Start | fast cold starts for real-time interactions | 0.5-3s | <30s (Fargate) | None | None |
| Max Request Duration | 15 mins for synchronous request, 8 hours for asynchronous requests | 15 min | Unlimited | Unlimited | Unlimited |
| WebSocket Support | Limited (For browser interaction) | Limited | Native | Native | Native |
| Deployment Speed | Fast | Fast | Medium | Slow | Slow |
| Portability | AWS-only | AWS-specific | High | Highest | Low |
| Monitoring | Built-in | Built-in | Integrated | Rich ecosystem | Custom |
| Multi-tenancy | Service-level | Function-level | Service-level | Namespace-level | Custom |
| Customization | Limited | Limited | High | Full | Full |
| Auth Support | SigV4, OAuth and JWT validation | Rich (Through API Gateway) | Rich (Through API Gateway) | Rich (Through API Gateway ) | Rich (Through API Gateway or ALB) |
