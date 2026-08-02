---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-fargate-spot-compared-to-reserved-instances.html
---

# AWS Fargate Spot compared to reserved instances
<a name="aws-fargate-spot-compared-to-reserved-instances"></a>

With Amazon ECS on AWS Fargate capacity providers, you can use [both Fargate and Fargate Spot capacity](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html) with your Amazon ECS tasks. With Fargate Spot, you can run interruption tolerant Amazon ECS tasks at a rate that’s discounted compared to the Fargate price. When AWS needs the capacity back, tasks are interrupted with a 2-minute warning. When the Spot instances are terminated, ECS requests new Spot capacity, possibly from a different AZ to replace the reclaimed instances.

The default weights used for Fargate compared to Fargate Spot instances are defined through parameters in the solution source code `FARGATE_RESERVED_WEIGHT = 1` and `FARGATE_SPOT_WEIGHT = 1` respectively.
