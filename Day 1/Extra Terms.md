# ApexaiQ Topics – Explanation

## 1. Vulnerabilities

A **vulnerability** is a weakness in hardware, software, network configuration, or a system that could be exploited by an attacker.

**Example:**  
An old version of Windows with a known security flaw has a vulnerability.

### Important Terms

- **CVE** — Common Vulnerabilities and Exposures; identifier for a known vulnerability.
- **CVSS** — Common Vulnerability Scoring System; measures vulnerability severity.
- **NVD** — National Vulnerability Database; contains information about publicly known vulnerabilities.

---

## 2. ITAM — IT Asset Management

**ITAM = Information Technology Asset Management.**

ITAM means managing an organization's technology assets throughout their lifecycle.

### Examples

- Laptops
- Desktops
- Servers
- Routers and switches
- Software
- Cloud resources
- Databases
- Applications

### ITAM Lifecycle

**Discover → Identify → Track → Maintain → Assess Risk → Replace/Retire**

### Example

A company has 500 laptops.

ITAM helps the company:

1. Identify all 500 laptops.
2. Track their owners and locations.
3. Check warranties.
4. Check vulnerabilities.
5. Identify old or unsupported laptops.
6. Plan replacement.

---

## 3. Compliance

**Compliance means following required rules, policies, standards, or regulations.**

Examples:

- ISO 27001
- SOC 2
- GDPR
- NIST guidelines
- Internal security policies

### Example

Company policy says:

> All laptops must have supported operating systems and security updates.

If 20 laptops are running unsupported software, those devices can represent **compliance violations**.

---

## 4. ApexaiQ Risk Score

The **ApexaiQ Risk Score** helps quantify technology risk in an organization's IT environment.

Risk can consider:

- Vulnerabilities
- Obsolescence
- Maintenance
- Compliance
- Asset visibility

### Main Idea

> **Risk Score helps answer: "What should we fix first?"**

### Example

| Asset | Vulnerability | Obsolete? | Maintenance | Risk |
|---|---|---|---|---|
| Server A | High | No | Active | High |
| Laptop B | Low | Yes | Expired | Medium |
| Server C | None | No | Active | Low |

The organization can prioritize the highest-risk assets first.

---

## 5. IQ Level / Asset Intelligence

This refers to the quality and usefulness of asset information.

Having only:

> Server 101

is not very useful.

Better information would be:

> Server 101 → Vendor → OS → Version → Owner → Location → Warranty → Vulnerabilities → EOL → Maintenance

The more complete and enriched the information is, the better decisions an organization can make.

---

## 6. Audit

An **audit** is a systematic examination of systems, processes, assets, and controls to check whether they meet required standards or policies.

### Example

An auditor asks:

> Show me all servers running unsupported operating systems.

If asset data is clean and organized, the organization can answer quickly.

If asset visibility is poor, the same task may take days or weeks.

### Key Idea

> **Good asset visibility makes an organization more audit-ready.**

---

## 7. Hardware Obsolescence

**Obsolescence means becoming outdated or no longer suitable for use.**

Hardware may become obsolete when:

- The vendor stops selling it.
- Vendor support ends.
- Spare parts become difficult to obtain.
- Performance becomes insufficient.
- Security support ends.

### Example

A company has a server that is 10 years old.

Even if it still works, it may become:

**Old → Unsupported → Difficult to Maintain → Higher Risk**

---

## 8. Maintenance

Maintenance means keeping an IT asset operational and supported.

It can include:

- Warranty
- Vendor support
- Software updates
- Hardware repairs
- Security patches
- Firmware updates

### Example

If a server's support expires in December 2026, the IT team should know this beforehand and plan renewal or replacement.

---

## 9. Why Agentless?

This is an important ApexaiQ concept.

### Agent-Based Approach

A software agent is installed on each device.

```text
Laptop → Agent
Server → Agent
Desktop → Agent
Cloud VM → Agent
```

The agents collect information and send it to a management platform.

### Agentless Approach

In an agentless approach, a traditional permanent software agent does not need to be installed on every endpoint.

### Advantages

- No agent installation on every device
- Faster deployment
- Less maintenance
- Lower endpoint overhead
- Useful for unmanaged/shadow asset discovery
- Can use APIs and existing data sources

### Interview Answer

> **ApexaiQ is agentless because it can discover and enrich asset information without requiring a traditional software agent on every endpoint, reducing deployment and maintenance overhead.**

---

## 10. N-MAP / Network Mapping

The handwritten note appears to refer to **network mapping/network discovery**.

Network mapping identifies:

- Devices
- Servers
- Routers
- Switches
- IP addresses
- Connections
- Network relationships

### Example

```text
Internet
   ↓
Firewall
   ↓
Router
   ↓
Switch
 ↓   ↓   ↓
PC  Server  Printer
```

The purpose is to understand **what exists on the network and how devices are connected**.

---

## 11. Containers

A **container** is a lightweight environment used to package and run an application together with its dependencies.

### Example

```text
Application
+ Libraries
+ Dependencies
+ Configuration
        ↓
     Container
```

**Docker** is a popular container technology.

In IT asset management, containers matter because organizations may have:

- Docker containers
- Kubernetes workloads
- Containerized applications

These can become part of the organization's technology estate and need visibility.

---

## 12. Crown Jewel Device / Asset

A **crown jewel asset** is a highly important asset whose compromise could seriously damage an organization.

### Examples

- Banking database
- Customer database
- Payment server
- Production server
- Authentication server
- Intellectual property repository

### Example

Suppose a company has:

**1,000 normal laptops + 1 payment database.**

The payment database is a **crown jewel**.

A vulnerability on that database should receive very high priority.

---

## 13. NVD

**NVD = National Vulnerability Database.**

NVD is maintained by **NIST** and provides information about publicly known cybersecurity vulnerabilities.

It contains information related to:

- CVEs
- CPEs
- CVSS
- Affected products
- Vulnerability descriptions

### Simple Definition

> **NVD = A large public database containing vulnerability information.**

---

## 14. CPE

**CPE = Common Platform Enumeration.**

CPE provides a standardized way to identify products and platforms.

Instead of simply saying:

> Microsoft Windows

a CPE can identify a specific vendor, product, and version.

### Relationship

```text
Asset
  ↓
Product + Version
  ↓
CPE
  ↓
NVD
  ↓
Vulnerability / CVE
```

This helps match products with known vulnerabilities.

---

## 15. CVE

**CVE = Common Vulnerabilities and Exposures.**

A CVE is a unique identifier for a publicly known vulnerability.

### Example

```text
CVE-2026-XXXXX
```

### Simple Definition

> **CVE = Vulnerability ID**

---

## 16. CVSS

**CVSS = Common Vulnerability Scoring System.**

CVSS measures vulnerability severity on a **0–10 scale**.

| Score | Severity |
|---:|---|
| 0 | None |
| 0.1–3.9 | Low |
| 4.0–6.9 | Medium |
| 7.0–8.9 | High |
| 9.0–10.0 | Critical |

### Example

A vulnerability with:

**CVSS = 9.8**

is generally much more urgent than:

**CVSS = 3.1**

### Remember

> **CVSS = Vulnerability Severity Score**

---

## 17. SLA Score

**SLA = Service Level Agreement.**

An SLA defines expected service levels and may include deadlines for resolving issues.

### Example

```text
Critical vulnerability → Fix within 24 hours
```

If fixed within 24 hours:

**SLA Met ✅**

If fixed after 5 days:

**SLA Breached ❌**

An SLA score can help measure whether service or remediation targets are being met.

---

## 18. CSV

**CSV = Comma-Separated Values.**

CSV is a simple format for storing tabular data.

### Example

```csv
Asset,IP,OS,Risk
Server01,10.0.0.1,Linux,High
Server02,10.0.0.2,Windows,Medium
```

CSV is useful for:

- Importing data
- Exporting data
- Reporting
- Data analysis
- Sharing information between systems

---

## 19. Modern Database of ApexaiQ

The handwritten note appears to refer to a modern database/platform used to store and process IT asset information.

Information can include:

```text
Devices
Software
Users
Networks
Vulnerabilities
Asset Relationships
Maintenance
Obsolescence
Compliance
```

### Basic Flow

**Collect → Normalize → Enrich → Analyze → Report**

---

## 20. IDs / CVE IDs / Asset IDs

The handwritten note is not completely clear.

If it refers to **CVE IDs**:

> A CVE ID uniquely identifies a publicly known vulnerability.

If it refers to **Asset IDs**:

> An Asset ID uniquely identifies a device or asset in an ITAM system.

### Example

```text
Asset ID: AST-1024
Device: Dell PowerEdge Server
IP: 192.168.1.10
Owner: IT Department
Risk: High
```

---

## 21. ApexaiQ Competitors

For research, ApexaiQ can be compared with platforms in ITAM, IT operations, asset discovery, and security.

Examples worth researching:

- ServiceNow
- Flexera
- Device42
- Lansweeper
- Ivanti

These products do not all have exactly the same focus, so comparison should be feature-by-feature.

### Important Comparison Points

| Feature | ApexaiQ |
|---|---|
| Asset discovery | Yes |
| Agentless approach | Yes |
| Vulnerability enrichment | Yes |
| Obsolescence tracking | Yes |
| Maintenance visibility | Yes |
| Compliance | Yes |
| Risk scoring | Yes |
| Data enrichment | Yes |
| CSV / Reporting | Yes |

---

## 22. ApexaiQ as a Product / SaaS Platform

ApexaiQ can be understood as a **SaaS-based product/platform**.

**SaaS = Software as a Service.**

Customers access the platform as a service rather than managing the entire application infrastructure themselves.

### Simple Definition

> **ApexaiQ is a SaaS-based, agentless asset-assurance platform focused on discovering and enriching IT asset information and helping organizations understand and reduce technology risk.**

---

# How Everything Connects

The most important concept is understanding the complete flow:

```text
             IT ENVIRONMENT
                   ↓
       ┌─────────────────────┐
       │  Asset Discovery    │
       │ Agentless / Sources │
       └──────────┬──────────┘
                  ↓
          Asset Information
                  ↓
          Data Normalization
                  ↓
            Data Enrichment
          ↙       ↓       ↘
      CPE/NVD  Maintenance  EOL
        ↓         ↓          ↓
      CVEs     Support    Obsolescence
        ↓
      CVSS
        ↓
  Vulnerability Risk
        ↓
 ┌───────────────────┐
 │ ApexaiQ Risk Score│
 └─────────┬─────────┘
           ↓
   Prioritize Actions
           ↓
    Fix / Replace / Patch
           ↓
    Lower Technology Risk
```

---

# One-Line Interview Answer

> **ApexaiQ discovers an organization's IT assets, enriches their data with vulnerability, lifecycle, maintenance, and compliance information, assesses the resulting risk, and helps IT teams prioritize actions.**

---

# Quick Revision

| Term | Meaning |
|---|---|
| ITAM | Information Technology Asset Management |
| Vulnerability | Weakness that can be exploited |
| CVE | Identifier for a known vulnerability |
| CVSS | Vulnerability severity scoring system |
| CPE | Standardized product/platform identification |
| NVD | National Vulnerability Database |
| SLA | Service Level Agreement |
| CSV | Comma-Separated Values |
| EOL | End of Life |
| Compliance | Following required rules/standards |
| Audit | Examination of systems/processes/controls |
| Obsolescence | Technology becoming outdated |
| Agentless | No traditional agent required on every endpoint |
| Crown Jewel | Highly critical/high-value asset |
| ITAM Lifecycle | Discover → Track → Maintain → Assess → Retire |
| SaaS | Software as a Service |
| Risk Score | Helps prioritize what should be fixed first |

---

## Topics That Need a Clearer Photo

A few handwritten terms are difficult to read accurately from the photo, especially:

- "N-MAP"
- "ST buckets"
- "C-ID's"
- "C9/C0 1,2,3"
- "modem database"

These should be confirmed from a clearer/closer photo before treating them as exact terminology.
