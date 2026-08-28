---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/building-prepare.html
---

# Preparing a dataset
<a name="building-prepare"></a>

If you have not done so already, prepare a detailed dataset of the websites that you want to collect information from. This dataset should include website URL domain names and relevant subdomain names. This section provides a step-by-step process for building this dataset.

## To prepare a dataset
<a name="to-prepare-a-dataset.7b31240c-357f-5e85-b569-5cf60f2df6c5"></a>

1. **Define the scope** – Determine the industry or sectors you're focusing on. Decide how many companies to include. And define any criteria that you want to collect about these companies, such as the number of employees, location, or revenue.

1. **Identify data sources** – Identify what sources of information you can use to collect information about these companies. Examples include business directories (such as [Crunchbase](https://www.crunchbase.com/), [Bloomberg](https://www.bloomberg.com/), or [Forbes](https://www.forbes.com/)), stock exchanges (such as NYSE and NASDAQ), industry-specific associations or publications, or government databases (such as SEC filings).

1. **Create a table** – In your preferred tool, such as Microsoft Excel, Google Sheets, or a database management system, create a table for collecting criteria about each company. Include a column for each criterion. At a minimum, include columns for the company name, primary domain, subdomains, industry, size, and location.

1. **Collect initial company information** – Collect the following information about each company and enter it into the table that you created:
   + Company name
   + Industry or sector
   + Company size (number of employees)
   + Revenue
   + Location of company headquarters

1. **Gather domain information** – For each company, extract the primary domain name from the main website URL, such as `example.com`. You can verify the domain information by using a WHOIS domain lookup tool.

1. **Gather subdomain information** – For each company, research the registered subdomains, such as `blog.example.com`. You can use subdomain enumeration tools, such as [Sublist3r](https://github.com/aboul3la/Sublist3r), [OWASP Amass](https://github.com/owasp-amass/amass), or [Subfinder](https://github.com/projectdiscovery/subfinder). You can perform Google dorking (by searching `site:example.com`), check DNS records by using a `dig` command or a DNS lookup tool, or you can analyze SSL or TLS certificates.

1. **Validate and clean the data** ­– Review, verify, and standardize the data that you've collected. For example, remove any duplicate entries, remove unnecessary URL information from domains and subdomains, and verify that all domains and subdomains are active.

1. **(Optional) Categorize the subdomains** – You can categorize the subdomains into types. The following are some examples of categories you might encounter:
   + Blogs, such as `blog.example.com`
   + Support or help, such as `support.example.com` or `help.example.com`
   + E-commerce, such as `shop.example.com` or `store.example.com`
   + Developer resources, such as `dev.example.com` or `api.example.com`
   + Regions or locations, such as `us.example.com` or `uk.example.com`

1. **(Optional) Add relevant metadata** – You can record any relevant metadata in the dataset. For example, you can add the last updated date, the source of information, or your confidence score for subdomain accuracy.

1. **Implement version control** – Use a version control system, such as Git, to track changes to the table over time. Back up the dataset regularly.

1. **Maintain the table** – Set up a schedule, such as quarterly, for updating the table. Standardize and implement a process for adding new companies or removing those you no longer need. When possible, automate discovery of subdomains.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
