---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/failure-mode-effects-analysis/appendix-fmea-spreadsheet-template.html
---

# Appendix: FMEA spreadsheet template
<a name="appendix-fmea-spreadsheet-template"></a>

The following table is a sample Failure Mode and Effects Analysis (FMEA) register pre-populated with common AWS service failure modes. Use it as a starting point for your own analysis. Adjust the severity, occurrence, and detection scores to reflect your application architecture and business context, and add rows as you identify new failure modes during sprint planning.

|
|
| **ID** | **Component** | **Failure mode** | **S** | **O** | **D** | **RPN** | **Recommended action** | **Owner** | **Timeline** | **Status** |
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1 | API Gateway | Throttling active | 7 | 6 | 4 | 168 | Implement circuit breaker | DevOps | Sprint 1 | Pending |
| 2 | Amazon RDS database | Connection timeout | 9 | 5 | 3 | 135 | Optimize pool \+ monitoring | Backend | Sprint 1 | Pending |
| 3 | Lambda function | Cold start delay | 5 | 8 | 6 | 240 | Implement warm-up | Backend | Sprint 1 | Pending |
| 4 | Amazon S3 | Access denied | 6 | 3 | 7 | 126 | Review IAM policies | DevOps | Sprint 2 | Pending |
| 5 | ElastiCache | Cache miss | 4 | 7 | 5 | 140 | Optimize cache strategy | Backend | Sprint 2 | Pending |
| 6 | CloudFront | SSL cert expired | 9 | 2 | 8 | 144 | Automate cert renewal | DevOps | Sprint 1 | Pending |
| 7 | Amazon ECS  | Container crash | 8 | 4 | 4 | 128 | Memory profiling \+ limits | DevOps | Sprint 2 | Pending |
| 8 | DynamoDB | Throttling | 6 | 5 | 3 | 90 | Configure auto scaling | Backend | Sprint 3 | Pending |
| 9 | Amazon SQS queue | Message loss | 8 | 3 | 6 | 144 | Implement retry logic | Backend | Sprint 2 | Pending |
| 10 | Route 53 | DNS resolution fail | 9 | 2 | 7 | 126 | Multiple health checks | DevOps | Sprint 2 | Pending |
| 11 | Amazon EC2 instance | Instance failure | 8 | 3 | 4 | 96 | Multi-AZ deployment | DevOps | Sprint 3 | Pending |
| 12 | Application Load Balancer | Health check failure | 7 | 4 | 3 | 84 | Custom health check | DevOps | Sprint 3 | Pending |
| 13 | Amazon Cognito | Auth failure | 6 | 5 | 5 | 150 | Implement auto refresh | Frontend | Sprint 2 | Pending |
| 14 | CloudWatch | Metric delay | 5 | 6 | 7 | 210 | Custom metrics \+ batching | DevOps | Sprint 1 | Pending |
| 15 | Amazon VPC | Network partition | 9 | 2 | 6 | 108 | Multi-AZ architecture | DevOps | Sprint 2 | Pending |
