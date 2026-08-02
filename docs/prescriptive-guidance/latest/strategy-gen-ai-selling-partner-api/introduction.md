---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/introduction.html
---

# Enabling business reporting and generative AI capabilities for Amazon selling partners
<a name="introduction"></a>

*Manikanta Gona and Hina Vinayak, Amazon Web Services*

## Business overview
<a name="business-overview"></a>

Amazon is a data-driven company. It provides a wealth of data to both Amazon vendors and sellers through various offerings, such as Vendor Central, Seller Central, electronic data interchange (EDI) solutions, and APIs.

In the [Amazon Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/welcome), *analytics reports* empower sellers and vendors to deeply analyze their sales performance, inventory health, glance views, and more. Comprehensive reports cover sales, traffic, net pure profit margin (net PPM), forecasting, inventory, and catalog management. Furthermore, *brand analytics reports* are a crucial component of this data-driven strategy, offering invaluable insights to first-party and third-party sellers. Third-party sellers also gain powerful insights through customer loyalty analytics and search analytics.

By providing these robust analytics and reporting capabilities, Amazon helps its selling partners to make informed, data-driven decisions that can drive their business growth and success on the Amazon marketplace. However, navigating and analyzing these extensive datasets can be challenging for some vendors and sellers.

## Solution overview
<a name="solution-overview"></a>

You can use generative artificial intelligence (generative AI) and analytics services to enhance your business reporting for the Amazon marketplace. [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) and [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) can help you analyze data from the Selling Partner API and improve your business reporting. By implementing data analytics and generative AI capabilities, you can unlock deeper insights, automate repetitive tasks, and enhance your customer experience on Amazon. This ultimately drives more sales and growth for your business.

The following is an overview of the data analytics, DevOps, and generative AI capabilities that you can gain by implementing the recommendations in this guide:
+ Create custom reports and interactive dashboards that unlock insights from your Selling Partner API data.
+ Develop secure, scalable extract, transform, and load (ETL) pipelines that ingest, transform, and load the data.
+ Combine Amazon Q with other business intelligence (BI) solutions to generate advanced analytics, forecast, and make data-driven decisions.
+ Build custom machine learning (ML) models that analyze your Selling Partner API data.
+ Use generative AI to automatically create optimized, high-quality product descriptions for your Amazon listings.
+ Use large language models (LLMs) to generate engaging, persuasive content, such as marketing copy and customer communications.
+ Use machine learning to forecast sales, inventory, and other key business metrics.

To implement these capabilities, you do the following:

1. **Integrate the Selling Partner API **– Set up secure connections to the Selling Partner APIs to access your sales, inventory, customer, and other business-critical data.

1. **Build data pipelines **– Develop robust ETL pipelines to normalize, structure, and prepare your Amazon data for analysis and modeling.

1. **Use Amazon Q and other analytics services** – Combine Amazon Q with complementary BI and data science services to create a comprehensive analytics ecosystem.

1. **Explore generative AI services** – Evaluate the AWS AI services and integrate them into your workflows to automate content generation, product descriptions, and predictive modeling.

1. **Implement AWS best practices** – Use AWS services, such as AWS Lake Formation and Amazon DataZone, to manage and govern your data according to your compliance requirements and AWS best practices.
