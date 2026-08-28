---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/next-steps.html
---

# Next steps and resources
<a name="next-steps"></a>

After collecting the raw environmental, social, and governance (ESG) data, you can do the following to extract meaningful information from the data:

1. **Clean the data** – The data might include a significant amount of irrelevant information that is unrelated to ESG factors and financial data. It is important to remove this irrelevant data and retain only the information needed to perform the required analytics. You can use tools, such as like [yfinance](https://pypi.org/project/yfinance/), to help clean the data.

1. **Extract and transform the data** – Extract the relevant features or variables from the raw data and transform them into a format that is suitable for analysis. You can transform the data into tabular format for better readability and clarity. You can use a library, such as [pandas](https://pandas.pydata.org/), to refine the data. You can also use feature engineering, data normalization, and derived metrics to transform the data.

1. **Perform analytics** – You can perform various analytical tasks. This might include generating descriptive statistics, creating data visualizations, and conducting exploratory data analysis to gain insights into the ESG performance of the companies.

1. **Apply machine learning** – You can use the cleaned and transformed data to train machine learning models. These models can help you identify companies that are currently demonstrating financial sustainability and project their future sustainability performance.

By using the web crawler and this data evaluation process, you can effectively gain a comprehensive understanding of the sustainability practices and financial performance of the companies you are evaluating. You can use this information to inform investment decisions, track progress, and support sustainable business practices.

## Resources
<a name="next-steps-resources"></a>
+ [What is a web crawler?](https://www.cloudflare.com/en-gb/learning/bots/what-is-a-web-crawler/) (Cloudflare website)
+ [Guide to ESG investment](https://www.investopedia.com/terms/e/environmental-social-and-governance-esg-criteria.asp) (Investopedia website)

## Tools
<a name="next-steps-tools"></a>
+ [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (Beautiful Soup documentation)
+ [Handling tabular, relational data](https://pandas.pydata.org/) (pandas website)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
