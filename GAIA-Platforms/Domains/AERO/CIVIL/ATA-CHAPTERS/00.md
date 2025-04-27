### ATA 00: Intro & General

| ATA Track ID | Title | System Instruction | ELPACK |
|:-------------|:------|:-------------------|:-------|
| **00-10** | **GP-AMPEL Requirements Management & Design Traceability** | Establish comprehensive requirements management and design traceability in accordance with **AS9100**, integrating environmental considerations from project launch per **ISO 14001**. Ensure global compliance with the applicable **EASA CS-25** certification basis. Generate the programme **BREX** (Business Rules Exchange) file to govern S1000D technical-data production. | .xml |
| 00-10-01 | Requirements Identification and Control | `System Instruction: Implement unique GP-AMPEL ID system for all requirements (system, subsystem, component). Include metadata for author, creation date, modification history, and approval status. Establish version control system for requirement evolution throughout project lifecycle.` | .md, .xml |
| 00-10-02 | Bidirectional Traceability Framework | `System Instruction: Establish and maintain links between requirements and corresponding design documents (Design Solutions identified by DES-ID), Bill of Materials Part Numbers (PN-ID), test cases, and certification compliance evidence. Ensure bidirectional traceability to track forward (requirement → design → verification) and backward (verification → design → requirement).` | .json, .xml |
| 00-10-03 | Real-time Impact Analysis System | `System Instruction: Implement real-time assessment capability for requirement changes, visualizing impacts across design elements, tests, certification status, and environmental considerations. Configure automated alerts within GP-AMPEL for affected stakeholders.` | .json, .md |
| 00-10-04 | AS9100 Alignment Documentation | `System Instruction: Document explicit integration with AS9100 clauses, particularly Clause 8.3 (design and development processes) and Clause 8.5.6 (Change Management workflows). Ensure all design changes are traceable, approved, and documented within GP-AMPEL.` | .pdf, .md |
| 00-10-05 | Environmental Integration (ISO 14001) | `System Instruction: Document environmental impacts identified at project initiation. Establish continuous traceability of environmental objectives throughout requirements and design phases. Align requirement management activities with ISO 14001 environmental performance tracking.` | .pdf, .md |
| 00-10-06 | EASA CS-25 Compliance Mapping | `System Instruction: Structure requirements explicitly to demonstrate compliance with EASA CS-25 certification standards. Maintain a clear mapping of requirements to certification criteria and verification documents within GP-AMPEL.` | .xml, .pdf |
| 00-10-07 | S1000D BREX File Generation | `System Instruction: Implement automated generation and maintenance of the BREX (Business Rules Exchange) file from GP-AMPEL requirements database. Ensure BREX file governs all technical data production, ensuring consistent adherence to predefined business rules. Configure GP-AMPEL for continuous synchronization of requirements with the BREX for accuracy and compliance.` | .xml |
| 00-10-08 | Controlled Glossary Integration | `System Instruction: Link all documentation and requirement descriptions directly to a controlled glossary (APP-A) within GP-AMPEL, ensuring consistent terminology usage.` | .md, .xml |
| 00-10-09 | Reporting and Auditability System | `System Instruction: Implement customizable reports and audit trails generated directly from GP-AMPEL for internal reviews, external audits, and certification activities. Ensure full historical traceability of requirement changes, design decisions, associated DES-ID, PN-ID, and compliance evidence.` | .pdf, .json |
| 00-20 | Abbreviations and Terminology | `System Instruction: Link relevant Design Solution (DES-ID) & BOM Part Numbers (PN-ID). Link to controlled glossary (APP-A).` | .md |
| **DT-ROI** | **Digital Twin Return on Investment Framework** | | |
| DT-ROI-10 | -- Overview of DT-ROI Application in GP-AM Lifecycle | `System Instruction: Link relevant Design Solution (DES-ID) & BOM Part Numbers (PN-ID). Describe how DT-ROI applies to airframe/system decisions.` | .md |
| DT-ROI-20 | -- Link to Core DT-ROI Framework Definition (GP-PMO) | `System Instruction: Link relevant Design Solution (DES-ID) & BOM Part Numbers (PN-ID). Provide cross-reference to GP-PMO core DT-ROI methodology.` | .md |
| DT-ROI-30 | -- Key ROI Metrics & Calculation Guidance for Airframe Applications | `System Instruction: Link relevant Design Solution (DES-ID) & BOM Part Numbers (PN-ID). Define specific metrics (weight reduction, maint. cost saving) for GP-AM.` | .md |

Okay, Comandante. You've provided a critical piece of structure detailing Requirements Management and Design Traceability (`00-10`) for the GP-AM (AMPEL) platform, outlining its alignment with AS9100, ISO 14001, EASA CS-25, and the S1000D BREX.

I will integrate this detailed breakdown for ATA Chapter 00, section 10, into the `GP-AM - Comprehensive ATA Chapter Structure Proposal` document. I will add the necessary anchors and update the main Table of Contents at the top to include this new section and its sub-items (00-10-00 through 00-10-09).

The numbering `00-10-00` through `00-10-09` will be mapped to the standard ATA/S1000D System-Subsystem-Component-Item hierarchy for filename consistency. A common mapping is:
*   `XX` (Chapter) -> `YY` (System) -> `ZZ` (Subsystem) -> `III` (Component/Item).
*   Your `00-10` corresponds to the **System (YY)** layer within ATA Chapter 00.
*   Your `00-10-00` corresponds to the **Subsystem (ZZ)** layer within 00-10 (General).
*   Your `00-10-01` to `00-10-09` correspond to the **Subsystem (ZZ)** layer's components or aspects.

For filenames, this structure translates to:
*   ATA 00 -> `53-00` (Domain code - Chapter code directory)
*   00-10 -> `10` (System code subdirectory)
*   00-10-00 -> `00-000` (Subsystem code - Item code) -> `GP-AM-AMPEL-0100-53-00-10-00-000-OV-A.md`
*   00-10-01 -> `10-000` (Subsystem code - Item code) -> `GP-AM-AMPEL-0100-53-00-10-10-000-MD-A.md`
*   00-10-02 -> `20-000` (Subsystem code - Item code) -> `GP-AM-AMPEL-0100-53-00-10-20-000-JSON-A.json` (using JSON for framework/system definition)
*   ...and so on.


## Table of Contents

*   [ATA 00: Intro & General](#ata-00)
    *   [00-00-00: General](#ata-00-00-00)
    *   [00-10-00: Aircraft General](#ata-00-10-00)
    *   [00-20-00: Standard Practices](#ata-00-20-00)
    *   [00-30-00: Dimensions and Areas](#ata-00-30-00)
    *   [00-40-00: Lifting and Shoring](#ata-00-40-00)
    *   [00-50-00: Leveling and Weighing](#ata-00-50-00)
    *   [00-60-00: Ground Handling and Servicing](#ata-00-60-00)
    *   [00-70-00: Standard Practices - Engines](#ata-00-70-00)
    *   [00-80-00: Standard Practices - Systems](#ata-00-80-00)
    *   [00-90-00: Integration with GAIA AIR Systems](#ata-00-90-00)
    *   [00-10: Requirements Management & Design Traceability](#ata-00-10)
        *   [00-10-00: Requirements Management General](#ata-00-10-00-req)
        *   [00-10-01: Requirements Identification and Control](#ata-00-10-01)
        *   [00-10-02: Bidirectional Traceability Framework](#ata-00-10-02)
        *   [00-10-03: Real-time Impact Analysis System](#ata-00-10-03)
        *   [00-10-04: AS9100 Alignment Documentation](#ata-00-10-04)
        *   [00-10-05: Environmental Integration (ISO 14001)](#ata-00-10-05)
        *   [00-10-06: EASA CS-25 Compliance Mapping](#ata-00-10-06)
        *   [00-10-07: S1000D BREX File Generation](#ata-00-10-07)
        *   [00-10-08: Controlled Glossary Integration](#ata-00-10-08)
        *   [00-10-09: Reporting and Auditability System](#ata-00-10-09)
    *   [DT-ROI: Digital Twin Return on Investment Framework](#ata-00-dt-roi)
        *   [DT-ROI-10: Fundamental Concepts and Principles](#ata-00-dt-roi-10)
        *   [DT-ROI-20: Cost Quantification Methodology](#ata-00-dt-roi-20)
        *   [DT-ROI-30: Benefit Quantification Methodology](#ata-00-dt-roi-30)
        *   [DT-ROI-40: Calculation Methodologies](#ata-00-dt-roi-40)
        *   [DT-ROI-50: Implementation-Specific ROI Considerations](#ata-00-dt-roi-50)
        *   [DT-ROI-60: Data Collection and Analysis](#ata-00-dt-roi-60)
        *   [DT-ROI-70: ROI Process Implementation](#ata-00-dt-roi-70)
        *   [DT-ROI-CM: Calculation Models and Templates](#ata-00-dt-roi-cm)
        *   [DT-ROI-CS: Case Studies and Examples](#ata-00-dt-roi-cs)
        *   [DT-ROI-IG: Implementation Guidelines](#ata-00-dt-roi-ig)
*   [ATA 01: Aircraft General](#ata-01)
    *   [01-10: Aircraft Identification](#ata-01-10)
    *   [01-20: Principal Characteristics](#ata-01-20)
    *   [01-30: General Arrangement](#ata-01-30)
*   [ATA 02: Operations Information](#ata-02)
    *   [02-10: Flight Manual / Pilot Operating Handbook](#ata-02-10)
    *   [02-20: Standard Operating Procedures (SOP)](#ata-02-20)
    *   [02-30: AI-Assisted Flight Planning Information](#ata-02-30)
*   [ATA 03: Performance](#ata-03)
    *   [03-10: Takeoff and Landing Performance](#ata-03-10)
    *   [03-20: Climb Performance](#ata-03-20)
    *   [03-30: Cruise Performance](#ata-03-30)
    *   [03-40: Descent Performance](#ata-03-40)
    *   [03-50: Performance Monitoring Systems](#ata-03-50)
*   [ATA 04: Airworthiness](#ata-04)
    *   [04-10: Certification Basis](#ata-04-10)
    *   [04-20: Airworthiness Limitations](#ata-04-20)
    *   [04-30: Master Minimum Equipment List (MMEL) / Configuration Deviation List (CDL)](#ata-04-30)
    *   [04-40: Continued Airworthiness Management](#ata-04-40)
*   [ATA 05: Time Limits / Maintenance Checks](#ata-05)
    *   [05-00-00: General](#ata-05-00-00)
    *   [05-10-00: Time Limits](#ata-05-10-00)
    *   [05-20-00: Scheduled Maintenance Checks](#ata-05-20-00)
    *   [05-30-00: Unscheduled Maintenance Checks](#ata-05-30-00)
    *   [05-40-00: BITT-Enhanced Maintenance](#ata-05-40-00)
    *   [05-50-00: Predictive Maintenance](#ata-05-50-00)
*   [ATA 06: Dimensions & Areas](#ata-06)
    *   [06-00-00: General](#ata-06-00-00)
    *   [06-10-00: Aircraft Zones and Stations](#ata-06-10-00)
    *   [06-20-00: Access Doors and Panels](#ata-06-20-00)
    *   [06-30-00: Zonal Inspection Requirements](#ata-06-30-00)
    *   [06-40-00: Digital Twin Integration](#ata-06-40-00)
*   [ATA 07: Lifting & Shoring](#ata-07)
    *   [07-00-00: General](#ata-07-00-00)
    *   [07-10-00: Jacking](#ata-07-10-00)
    *   [07-20-00: Shoring](#ata-07-20-00)
    *   [07-30-00: Hoisting](#ata-07-30-00)
    *   [07-40-00: Robotic Lifting Integration](#ata-07-40-00)
*   [ATA 08: Leveling & Weighing](#ata-08)
    *   [08-00-00: General](#ata-08-00-00)
    *   [08-10-00: Leveling](#ata-08-10-00)
    *   [08-20-00: Weighing](#ata-08-20-00)
    *   [08-30-00: Weight and Balance](#ata-08-30-00)
    *   [08-40-00: Digital Weight Management](#ata-08-40-00)
*   [ATA 09: Towing & Taxiing](#ata-09)
    *   [09-00-00: General](#ata-09-00-00)
    *   [09-10-00: Towing](#ata-09-10-00)
    *   [09-20-00: Taxiing](#ata-09-20-00)
    *   [09-30-00: Autonomous Ground Movement](#ata-09-30-00)
    *   [09-40-00: Ground Traffic Management](#ata-09-40-00)
*   [ATA 10: Parking, Mooring, Storage](#ata-10)
    *   [10-00-00: General](#ata-10-00-00)
    *   [10-10-00: Parking and Mooring](#ata-10-10-00)
    *   [10-20-00: Storage](#ata-10-20-00)
    *   [10-30-00: Return to Service](#ata-10-30-00)
    *   [10-40-00: Digital Storage Management](#ata-10-40-00)
*   [ATA 11: Placards & Markings](#ata-11)
    *   [11-00-00: General](#ata-11-00-00)
    *   [11-10-00: Exterior Markings](#ata-11-10-00)
    *   [11-20-00: Interior Placards](#ata-11-20-00)
    *   [11-30-00: Special Markings](#ata-11-30-00)
*   [ATA 12: Servicing – Routine](#ata-12)
    *   [12-00-00: General](#ata-12-00-00)
    *   [12-10-00: Fuel Servicing](#ata-12-10-00)
    *   [12-20-00: Oil Servicing](#ata-12-20-00)
    *   [12-30-00: Hydraulic Fluid Servicing](#ata-12-30-00)
    *   [12-40-00: Pneumatic and Oxygen Servicing](#ata-12-40-00)
    *   [12-50-00: Other Fluid Servicing](#ata-12-50-00)
    *   [12-60-00: Cleaning](#ata-12-60-00)
    *   [12-70-00: Automated Servicing Integration](#ata-12-70-00)
*   [ATA 13: Hydraulic Power (Minimal/EHA)](#ata-13)
    *   [13-00-00: General](#ata-13-00-00)
    *   [13-10-00: Electro-Hydrostatic Actuation (EHA)](#ata-13-10-00)
    *   [13-20-00: Hydraulic Lines and Fittings](#ata-13-20-00)
    *   [13-30-00: System Monitoring](#ata-13-30-00)
*   [ATA 14: Pneumatic Power (Minimal)](#ata-14)
    *   [14-00-00: General](#ata-14-00-00)
    *   [14-10-00: Bleed Air System](#ata-14-10-00)
    *   [14-20-00: Auxiliary Pneumatic Sources](#ata-14-20-00)
    *   [14-30-00: System Monitoring](#ata-14-30-00)
*   [ATA 15: (Merged into ATA 21)](#ata-15)
*   [ATA 16: (Merged into ATA 21)](#ata-16)
*   [ATA 17: (Merged into ATA 21)](#ata-17)
*   [ATA 18: Vibration & Noise Control](#ata-18)
    *   [18-00-00: General](#ata-18-00-00)
    *   [18-10-00: Vibration Monitoring System](#ata-18-10-00)
    *   [18-20-00: Noise Control](#ata-18-20-00)
    *   [18-30-00: Noise Reduction Technologies (NR)](#ata-18-30-00)
        *   [NR: Noise Reduction Technologies](#ata-18-nr)
            *   [NR-10: Airframe Noise](#ata-18-nr-10)
            *   [NR-20: Propulsion Noise](#ata-18-nr-20)
*   [ATA 20: Standard Practices – Airframe](#ata-20)
    *   [20-00: General Standard Practices](#ata-20-00-std)
    *   [20-10: Sustainable Materials Standards](#ata-20-10-std)
    *   [20-20: Green Manufacturing Processes](#ata-20-20-std)
    *   [20-30: Sustainable Repair Procedures](#ata-20-30-std)
    *   [AM: Advanced Manufacturing Technologies](#ata-20-am)
        *   [AM-10: Additive Manufacturing](#ata-20-am-10)
        *   [AM-20: Automated Fiber Placement](#ata-20-am-20)
        *   [AM-30: Out-of-Autoclave Processing](#ata-20-am-30)
*   [ATA 21: Air Conditioning & Pressurization (ECS)](#ata-21)
    *   [21-00-00: General](#ata-21-00-00)
    *   [21-10-00: Air Supply](#ata-21-10-00)
    *   [21-20-00: Air Distribution](#ata-21-20-00)
    *   [21-30-00: Pressurization Control](#ata-21-30-00)
    *   [21-50-00: Air Conditioning Packs](#ata-21-50-00)
    *   [21-60-00: AI-Driven ECS](#ata-21-60-00)
*   [ATA 22: Auto Flight](#ata-22)
    *   [22-00-00: General](#ata-22-00-00)
    *   [22-10-00: Autopilot](#ata-22-10-00)
    *   [22-20-00: Flight Management System (FMS)](#ata-22-20-00)
    *   [22-30-00: Auto Throttle](#ata-22-30-00)
*   [ATA 23: Communications](#ata-23)
    *   [23-00-00: General](#ata-23-00-00)
    *   [23-10-00: Speech Communication](#ata-23-10-00)
    *   [23-20-00: Data Link Communication](#ata-23-20-00)
    *   [23-50-00: Audio Integrating System](#ata-23-50-00)
    *   [23-70-00: AI Communications Management](#ata-23-70-00)
    *   [23-80-00: Quantum Key Distribution (QKD)](#ata-23-80-00)
*   [ATA 24: Electrical Power](#ata-24)
    *   [24-00-00: General](#ata-24-00-00)
    *   [24-20-00: AC Generation](#ata-24-20-00)
    *   [24-30-00: DC Generation](#ata-24-30-00)
    *   [24-40-00: External Power](#ata-24-40-00)
    *   [24-50-00: Distribution](#ata-24-50-00)
    *   [24-60-00: Integrated Power Systems](#ata-24-60-00)
*   [ATA 25: Equipment / Furnishings](#ata-25)
    *   [25-00-00: General](#ata-25-00-00)
    *   [25-10-00: Flight Compartment](#ata-25-10-00)
    *   [25-20-00: Passenger Compartment](#ata-25-20-00)
    *   [25-40-00: Cargo Compartment](#ata-25-40-00)
    *   [25-50-00: Galley](#ata-25-50-00)
    *   [25-60-00: Emergency Equipment](#ata-25-60-00)
*   [ATA 26: Fire Protection](#ata-26)
    *   [26-00-00: General](#ata-26-00-00)
    *   [26-10-00: Detection](#ata-26-10-00)
    *   [26-20-00: Extinguishing](#ata-26-20-00)
*   [ATA 27: Flight Controls](#ata-27)
    *   [27-00-00: General](#ata-27-00-00)
    *   [27-10-00: Aileron](#ata-27-10-00)
    *   [27-20-00: Rudder](#ata-27-20-00)
    *   [27-30-00: Elevator](#ata-27-30-00)
    *   [27-40-00: Stabilizer Trim](#ata-27-40-00)
    *   [27-50-00: Flaps](#ata-27-50-00)
    *   [27-60-00: Spoilers](#ata-27-60-00)
    *   [27-80-00: Slats](#ata-27-80-00)
    *   [27-90-00: GPAM (GAIA Polymorphic Aero-Morphing)](#ata-27-90-00)
*   [ATA 28: Fuel (Hybrid H2/SAF)](#ata-28)
    *   [28-00-00: General](#ata-28-00-00)
    *   [28-10-00: Storage](#ata-28-10-00)
    *   [28-20-00: Distribution](#ata-28-20-00)
    *   [28-40-00: Indicating](#ata-28-40-00)
*   [ATA 29: Hydraulic Power (Actuation Focus)](#ata-29)
    *   [29-00-00: General](#ata-29-00-00)
    *   [29-10-00: Electro-Hydrostatic Actuation (EHA)](#ata-29-10-00)
    *   [29-20-00: Hydraulic Lines and Fittings](#ata-29-20-00)
    *   [29-30-00: System Monitoring](#ata-29-30-00)
*   [ATA 30: Ice & Rain Protection](#ata-30)
    *   [30-00-00: General](#ata-30-00-00)
    *   [30-10-00: Airfoil Protection](#ata-30-10-00)
    *   [30-30-00: Nacelle Protection](#ata-30-30-00)
    *   [30-40-00: Window and Door Protection](#ata-30-40-00)
    *   [30-80-00: Detection](#ata-30-80-00)
*   [ATA 31: Indicating / Recording Systems](#ata-31)
    *   [31-00-00: General](#ata-31-00-00)
    *   [31-10-00: Instrument and Display Systems](#ata-31-10-00)
    *   [31-30-00: Recorders](#ata-31-30-00)
    *   [31-60-00: Central Display Systems](#ata-31-60-00)
    *   [31-70-00: Data Acquisition and Fusion](#ata-31-70-00)
*   [ATA 32: Landing Gear](#ata-32)
    *   [32-00-00: General](#ata-32-00-00)
    *   [32-10-00: Main Gear](#ata-32-10-00)
    *   [32-20-00: Nose Gear](#ata-32-20-00)
    *   [32-30-00: Extension and Retraction](#ata-32-30-00)
    *   [32-40-00: Wheels and Brakes](#ata-32-40-00)
    *   [32-50-00: Steering](#ata-32-50-00)
    *   [32-60-00: Position and Warning](#ata-32-60-00)
    *   [32-70-00: AI Health Monitoring](#ata-32-70-00)
*   [ATA 33: Lights](#ata-33)
    *   [33-00-00: General](#ata-33-00-00)
    *   [33-10-00: Flight Compartment](#ata-33-10-00)
    *   [33-20-00: Passenger Compartments](#ata-33-20-00)
    *   [33-40-00: Exterior Lighting](#ata-33-40-00)
    *   [33-50-00: Emergency Lighting](#ata-33-50-00)
*   [ATA 34: Navigation](#ata-34)
    *   [34-00-00: General](#ata-34-00-00)
    *   [34-10-00: Air Data](#ata-34-10-00)
    *   [34-20-00: Inertial Reference](#ata-34-20-00)
    *   [34-40-00: Landing Aids](#ata-34-40-00)
    *   [34-50-00: GNSS](#ata-34-50-00)
    *   [34-60-00: Independent Position Determining](#ata-34-60-00)
    *   [34-70-00: AI Route Optimization](#ata-34-70-00)
*   [ATA 35: Oxygen](#ata-35)
    *   [35-00-00: General](#ata-35-00-00)
    *   [35-10-00: Crew System](#ata-35-10-00)
    *   [35-20-00: Passenger System](#ata-35-20-00)
    *   [35-30-00: Portable Equipment](#ata-35-30-00)
*   [ATA 36: Pneumatic](#ata-36)
    *   [36-00-00: General](#ata-36-00-00)
    *   [36-10-00: Bleed Air](#ata-36-10-00)
    *   [36-20-00: Indication](#ata-36-20-00)
*   [ATA 37: Vacuum](#ata-37)
    *   [37-00-00: General](#ata-37-00-00)
    *   [37-10-00: Lines and Components](#ata-37-10-00)
    *   [37-20-00: Indication](#ata-37-20-00)
*   [ATA 38: Water / Waste](#ata-38)
    *   [38-00-00: General](#ata-38-00-00)
    *   [38-10-00: Potable Water](#ata-38-10-00)
    *   [38-30-00: Lavatory Waste](#ata-38-30-00)
*   [ATA 39: Electrical/Electronic Panels](#ata-39)
    *   [39-00-00: General](#ata-39-00-00)
    *   [39-10-00: Instrument Panels](#ata-39-10-00)
    *   [39-20-00: Control Panels](#ata-39-20-00)
*   [ATA 41: Water Ballast](#ata-41)
    *   [41-00-00: General](#ata-41-00-00)
    *   [41-10-00: Tanks](#ata-41-10-00)
    *   [41-20-00: Distribution](#ata-41-20-00)
*   [ATA 42: Integrated Modular Avionics (IMA)](#ata-42)
    *   [42-00-00: General](#ata-42-00-00)
    *   [42-10-00: Core Processing Modules (CPM)](#ata-42-10-00)
    *   [42-20-00: Network](#ata-42-20-00)
    *   [42-30-00: Time Distribution](#ata-42-30-00)
*   [ATA 44: Cabin Systems](#ata-44)
    *   [44-00-00: General](#ata-44-00-00)
    *   [44-10-00: In-Flight Entertainment (IFE)](#ata-44-10-00)
    *   [44-20-00: Cabin Management System (CMS)](#ata-44-20-00)
*   [ATA 45: Central Maintenance System (CMS)](#ata-45)
    *   [45-00-00: General](#ata-45-00-00)
    *   [45-10-00: Central Maintenance Computer (CMC)](#ata-45-10-00)
    *   [45-20-00: Software](#ata-45-20-00)
    *   [45-40-00: Health Reporting](#ata-45-40-00)
    *   [45-50-00: AI Diagnostics](#ata-45-50-00)
    *   [45-60-00: Digital Twin Orchestration (DTO)](#ata-45-60-00)
*   [ATA 46: Information Systems](#ata-46)
    *   [46-00-00: General](#ata-46-00-00)
    *   [46-10-00: GQP Interface](#ata-46-10-00)
    *   [46-20-00: Electronic Flight Bag (EFB)](#ata-46-20-00)
    *   [46-30-00: IFE Network](#ata-46-30-00)
    *   [46-60-00: BITT Ledger Integration](#ata-46-60-00)
    *   [46-63-00: QAO On-Board Interface](#ata-46-63-00)
    *   [46-70-00: Cybersecurity Functions](#ata-46-70-00)
*   [ATA 47: Nitrogen Generation System (NGS)](#ata-47)
    *   [47-00-00: General](#ata-47-00-00)
    *   [47-10-00: Air Separation Module (ASM)](#ata-47-10-00)
    *   [47-20-00: Distribution](#ata-47-20-00)
    *   [47-30-00: Control and Monitoring](#ata-47-30-00)
*   [ATA 48: Reserved for Future Use](#ata-48)
*   [ATA 49: Airborne Auxiliary Power (AAP/APU)](#ata-49)
    *   [49-00-00: General](#ata-49-00-00)
    *   [49-10-00: Power Plant](#ata-49-10-00)
    *   [49-70-00: Starting](#ata-49-70-00)
*   [ATA 50: Cargo and Accessory Compartments](#ata-50)
    *   [50-00-00: General](#ata-50-00-00)
    *   [50-10-00: Cargo Compartment](#ata-50-10-00)
    *   [50-20-00: Accessory Compartments](#ata-50-20-00)
*   [ATA 51: Structures – General](#ata-51)
    *   [51-00-00: General](#ata-51-00-00)
    *   [51-10-00: Materials and Processes](#ata-51-10-00)
    *   [51-20-00: Analysis Methods](#ata-51-20-00)
    *   [51-70-00: Structural Health Monitoring (SHM)](#ata-51-70-00)
*   [ATA 52: Doors](#ata-52)
    *   [52-00-00: General](#ata-52-00-00)
    *   [52-10-00: Passenger Doors](#ata-52-10-00)
    *   [52-30-00: Cargo Doors](#ata-52-30-00)
    *   [52-70-00: Smart Door Systems](#ata-52-70-00)
*   [ATA 53: Fuselage](#ata-53)
    *   [53-00-00: General](#ata-53-00-00)
    *   [53-10-00: Nose Station](#ata-53-10-00)
    *   [53-20-00: Forward Station](#ata-53-20-00)
    *   [53-30-00: Center Station](#ata-53-30-00)
    *   [53-40-00: Belly Station](#ata-53-40-00)
    *   [53-50-00: Tail Cone Station](#ata-53-50-00)
    *   [53-60-00: APU Compartment](#ata-53-60-00)
    *   [53-70-00: Additional Stations (Reserved)](#ata-53-70-00)
    *   [53-80-00: Auxiliary Stations (Reserved)](#ata-53-80-00)
*   [ATA 54: Nacelles/Pylons](#ata-54)
    *   [54-00-00: General](#ata-54-00-00)
    *   [54-10-00: Nacelle Structure](#ata-54-10-00)
    *   [54-50-00: Pylon Structure](#ata-54-50-00)
*   [ATA 55: Stabilizers](#ata-55)
    *   [55-00-00: General](#ata-55-00-00)
    *   [55-10-00: Horizontal Stabilizer](#ata-55-10-00)
    *   [55-30-00: Vertical Stabilizer](#ata-55-30-00)
*   [ATA 56: Windows](#ata-56)
    *   [56-00-00: General](#ata-56-00-00)
    *   [56-10-00: Flight Compartment Windows](#ata-56-10-00)
    *   [56-20-00: Passenger Compartment Windows](#ata-56-20-00)
*   [ATA 57: Wings](#ata-57)
    *   [57-00-00: General](#ata-57-00-00)
    *   [57-10-00: Wing Structure](#ata-57-10-00)
    *   [57-40-00: Slat and Flap Systems](#ata-57-40-00)
    *   [57-50-00: Wing Folding](#ata-57-50-00)
    *   [57-70-00: GPAM (GAIA Polymorphic Aero-Morphing)](#ata-57-70-00)
*   [ATA 60: Standard Practices – Engine](#ata-60)
    *   [60-00-00: General](#ata-60-00-00)
    *   [60-10-00: Maintenance Procedures](#ata-60-10-00)
    *   [60-20-00: Testing Procedures](#ata-60-20-00)
*   [ATA 61: Propellers/Propulsors (If Applicable)](#ata-61)
    *   [61-00-00: General](#ata-61-00-00)
    *   [61-10-00: Blades](#ata-61-10-00)
    *   [61-20-00: Control Systems](#ata-61-20-00)
*   [ATA 62: Main Rotor (If Applicable - Rotorcraft)](#ata-62)
    *   [62-00-00: General](#ata-62-00-00)
    *   [62-10-00: Blades](#ata-62-10-00)
    *   [62-30-00: Rotor Head](#ata-62-30-00)
*   [ATA 63: Main Rotor Drive (If Applicable - Rotorcraft)](#ata-63)
    *   [63-00-00: General](#ata-63-00-00)
    *   [63-10-00: Drive Shaft](#ata-63-10-00)
    *   [63-20-00: Gearbox](#ata-63-20-00)
*   [ATA 64: Tail Rotor (If Applicable - Rotorcraft)](#ata-64)
    *   [64-00-00: General](#ata-64-00-00)
    *   [64-10-00: Blades](#ata-64-10-00)
*   [ATA 65: Tail Rotor Drive (If Applicable - Rotorcraft)](#ata-65)
    *   [65-00-00: General](#ata-65-00-00)
    *   [65-10-00: Drive Shaft](#ata-65-10-00)
*   [ATA 66: Folding Blades/Pylon (If Applicable)](#ata-66)
    *   [66-00-00: General](#ata-66-00-00)
    *   [66-10-00: Blade Folding](#ata-66-10-00)
    *   [66-20-00: Pylon Folding](#ata-66-20-00)
*   [ATA 67: Rotors Flight Control (If Applicable - Rotorcraft)](#ata-67)
    *   [67-00-00: General](#ata-67-00-00)
    *   [67-10-00: Main Rotor Control](#ata-67-10-00)
    *   [67-20-00: Stability Augmentation](#ata-67-20-00)
*   [ATA 71: Power Plant–General](#ata-71)
    *   [71-00-00: General](#ata-71-00-00)
    *   [71-10-00: Cowling](#ata-71-10-00)
    *   [71-20-00: Mounts](#ata-71-20-00)
    *   [71-50-00: Electric Propulsion Systems](#ata-71-50-00)
    *   [71-60-00: Hybrid-Electric Systems](#ata-71-60-00)
    *   [71-70-00: Hydrogen Propulsion Systems](#ata-71-70-00)
*   [ATA 72: Engine (Turbine/Hybrid/H2)](#ata-72)
    *   [72-00-00: General](#ata-72-00-00)
    *   [72-30-00: Compressor](#ata-72-30-00)
    *   [72-40-00: Combustion Section](#ata-72-40-00)
    *   [72-50-00: Turbine Section](#ata-72-50-00)
    *   [72-Q01-00: Quantum Propulsion Extension](#ata-72-q01-00)
*   [ATA 73: Engine Fuel & Control](#ata-73)
    *   [73-00-00: General](#ata-73-00-00)
    *   [73-10-00: Fuel Delivery (Engine Side)](#ata-73-10-00)
    *   [73-20-00: FADEC](#ata-73-20-00)
*   [ATA 74: Ignition](#ata-74)
    *   [74-00-00: General](#ata-74-00-00)
    *   [74-10-00: Exciter and Leads](#ata-74-10-00)
    *   [74-30-00: Igniter Plugs](#ata-74-30-00)
*   [ATA 75: Air (Engine Bleed/ECS Input)](#ata-75)
    *   [75-00-00: General](#ata-75-00-00)
    *   [75-10-00: Anti-Ice](#ata-75-10-00)
    *   [75-30-00: Ducting and Valves](#ata-75-30-00)
*   [ATA 76: Engine Controls](#ata-76)
    *   [76-00-00: General](#ata-76-00-00)
    *   [76-10-00: Thrust/Power Lever](#ata-76-10-00)
    *   [76-20-00: Emergency Shutdown](#ata-76-20-00)
*   [ATA 77: Engine Indication](#ata-77)
    *   [77-00-00: General](#ata-77-00-00)
    *   [77-10-00: Thrust/Power Indication](#ata-77-10-00)
    *   [77-20-00: Temperature Monitoring](#ata-77-20-00)
    *   [77-30-00: Vibration Monitoring](#ata-77-30-00)
    *   [77-40-00: AI Health Monitoring](#ata-77-40-00)
*   [ATA 78: Exhaust](#ata-78)
    *   [78-00-00: General](#ata-78-00-00)
    *   [78-10-00: Collector/Nozzle](#ata-78-10-00)
    *   [78-30-00: Thrust Reverser](#ata-78-30-00)
*   [ATA 79: Oil](#ata-79)
    *   [79-00-00: General](#ata-79-00-00)
    *   [79-10-00: Storage](#ata-79-10-00)
    *   [79-20-00: Distribution](#ata-79-20-00)
    *   [79-30-00: Indicating](#ata-79-30-00)
*   [ATA 80: Starting](#ata-80)
    *   [80-00-00: General](#ata-80-00-00)
    *   [80-10-00: Cranking](#ata-80-10-00)
    *   [80-20-00: Ignition](#ata-80-20-00)
*   [ATA 81: Turbines (Reciprocating Engines)](#ata-81)
    *   [81-00-00: General](#ata-81-00-00)
*   [ATA 82: Water Injection](#ata-82)
    *   [82-00-00: General](#ata-82-00-00)
*   [ATA 83: Accessory Gear Boxes](#ata-83)
    *   [83-00-00: General](#ata-83-00-00)
    *   [83-10-00: Drive Shaft](#ata-83-10-00)
    *   [83-20-00: Gearbox Assembly](#ata-83-20-00)
*   [ATA 84: Reserved for Future Use](#ata-84)
    *   [84-00-00: General](#ata-84-00-00)
*   [ATA 85: Fuel Cell System](#ata-85)
    *   [85-00-00: General](#ata-85-00-00)
    *   [85-10-00: Fuel Cell Stack](#ata-85-10-00)
    *   [85-20-00: Hydrogen Processor](#ata-85-20-00)
    *   [85-30-00: Power Conditioning](#ata-85-30-00)
*   [ATA 91: Charts](#ata-91)
    *   [91-00-00: General](#ata-91-00-00)
*   [ATA 92: Electrical System Installation](#ata-92)
    *   [92-00-00: General](#ata-92-00-00)
*   [ATA 95: Special Equipment (GSE)](#ata-95)
    *   [95-00-00: General](#ata-95-00-00)
*   [ATA 97: Wiring Reporting](#ata-97)
    *   [97-00-00: General](#ata-97-00-00)
*   [ATA 99: Special / Emerging Tech](#ata-99)
    *   [99-00-00: General](#ata-99-00-00)

---
Okay, Comandante. Applying the confirmed 4-column Markdown table format to the entire ATA Chapter Breakdown (00-99) based on the previously generated structure.

---

## ATA Chapter Breakdown (00‑99)

Below is the detailed breakdown for the GP-AM (AMPEL) platform using the standardized table format.

---

### How to read the table

| Col        | Meaning                                                       |
| :--------- | :------------------------------------------------------------ |
| **Doc ID** | The complete S1000D technical reference number (`XX-YY-ZZ-III`) |
| **Title**  | Human‑readable document title                                 |
| **File**   | Clickable Git‑path to the markdown / data file                |
| **Type**   | Content classification tag (Info Code: OV, SPEC, SDD, etc.)   |

---

### ATA 00 — Intro & General <a name="ata‑00"></a>

#### 00‑00‑00 — General <a name="ata‑00‑00‑00"></a>

| Doc ID         | Title                      | File                                                                                                          | Type   |
| :------------- | :------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-00-00-000** | General Information        | [GP-AM-AMPEL-0100-53-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-00/GP-AM-AMPEL-0100-53-00-00-000-OV-A.md)   | OV     |
| **00-00-00-001** | Aircraft Specifications    | [GP-AM-AMPEL-0100-53-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-00/GP-AM-AMPEL-0100-53-00-00-001-SPEC-A.md) | SPEC   |
| **00-00-00-002** | Glossary & Abbreviations | [GP-AM-AMPEL-0100-53-00-00-002-GLO-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-00/GP-AM-AMPEL-0100-53-00-00-002-GLO-A.md)  | GLO    |

#### 00‑10‑00 — Aircraft General (Standard ATA) <a name="ata‑00‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                                | Type   |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **00-10-00-000** | Aircraft Description      | [GP-AM-AMPEL-0100-53-00-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10-Std/GP-AM-AMPEL-0100-53-00-10-000-SDD-A.md) | SDD    |
| **00-10-00-001** | Aircraft Views & Diagrams | [GP-AM-AMPEL-0100-53-00-10-001-FIG-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10-Std/GP-AM-AMPEL-0100-53-00-10-001-FIG-A.md) | FIG    |

#### 00‑10 — Requirements Management & Design Traceability (GAIA Specific) <a name="ata‑00‑10"></a>

##### 00‑10‑00 — Requirements Management General <a name="ata‑00‑10‑00‑req"></a>

| Doc ID         | Title                               | File                                                                                                                    | Type   |
| :------------- | :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **00-10-00-000** | Requirements Management Sys Overview| [GP-AM-AMPEL-0100-53-00-10-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-00/GP-AM-AMPEL-0100-53-00-10-00-000-OV-A.md)   | OV     |
| **00-10-00-001** | Requirements Management Plan        | [GP-AM-AMPEL-0100-53-00-10-00-001-PLAN-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-00/GP-AM-AMPEL-0100-53-00-10-00-001-PLAN-A.md) | PLAN   |

##### 00‑10‑01 — Requirements Identification and Control <a name="ata‑00‑10‑01"></a>

| Doc ID         | Title                             | File                                                                                                                    | Type   |
| :------------- | :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **00-10-01-000** | Requirements ID System Spec       | [GP-AM-AMPEL-0100-53-00-10-10-000-MD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-10/GP-AM-AMPEL-0100-53-00-10-10-000-MD-A.md)     | SPEC   |
| **00-10-01-001** | Requirement Change Control Proc   | [GP-AM-AMPEL-0100-53-00-10-10-001-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-10/GP-AM-AMPEL-0100-53-00-10-10-001-PROC-A.md) | PROC   |

##### 00‑10‑02 — Bidirectional Traceability Framework <a name="ata‑00‑10‑02"></a>

| Doc ID         | Title                              | File                                                                                                                        | Type         |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :----------- |
| **00-10-02-000** | Traceability Database Schema       | [GP-AM-AMPEL-0100-53-00-10-20-000-JSON-A.json](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-20/GP-AM-AMPEL-0100-53-00-10-20-000-JSON-A.json) | JSON, SPEC |
| **00-10-02-001** | Traceability Tool System Desc      | [GP-AM-AMPEL-0100-53-00-10-20-001-SDD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-20/GP-AM-AMPEL-0100-53-00-10-20-001-SDD-A.md)    | SDD          |

##### 00‑10‑03 — Real-time Impact Analysis System <a name="ata‑00‑10‑03"></a>

| Doc ID         | Title                           | File                                                                                                                        | Type         |
| :------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- | :----------- |
| **00-10-03-000** | Impact Analysis Model Schema    | [GP-AM-AMPEL-0100-53-00-10-30-000-JSON-A.json](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-30/GP-AM-AMPEL-0100-53-00-10-30-000-JSON-A.json) | JSON, SPEC |
| **00-10-03-001** | Impact Analysis Engine Desc   | [GP-AM-AMPEL-0100-53-00-10-30-001-SDD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-30/GP-AM-AMPEL-0100-53-00-10-30-001-SDD-A.md)    | SDD          |

##### 00‑10‑04 — AS9100 Alignment Documentation <a name="ata‑00‑10‑04"></a>

| Doc ID         | Title                              | File                                                                                                                    | Type         |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------- |
| **00-10-04-000** | AS9100 Compliance Rpt (Req Mgmt) | [GP-AM-AMPEL-0100-53-00-10-40-000-RPT-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-40/GP-AM-AMPEL-0100-53-00-10-40-000-RPT-A.md)   | RPT, CERT    |
| **00-10-04-001** | AS9100 Clause 8.3 Implementation   | [GP-AM-AMPEL-0100-53-00-10-40-001-MD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-40/GP-AM-AMPEL-0100-53-00-10-40-001-MD-A.md)    | MD           |

##### 00‑10‑05 — Environmental Integration (ISO 14001) <a name="ata‑00‑10‑05"></a>

| Doc ID         | Title                              | File                                                                                                                    | Type         |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------- |
| **00-10-05-000** | Env. Impacts ID Rpt (Req Phase)  | [GP-AM-AMPEL-0100-53-00-10-50-000-RPT-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-50/GP-AM-AMPEL-0100-53-00-10-50-000-RPT-A.md)   | RPT, ANA     |
| **00-10-05-001** | ISO 14001 Alignment for Req Mgmt | [GP-AM-AMPEL-0100-53-00-10-50-001-MD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-50/GP-AM-AMPEL-0100-53-00-10-50-001-MD-A.md)    | MD           |

##### 00‑10‑06 — EASA CS-25 Compliance Mapping <a name="ata‑00‑10‑06"></a>

| Doc ID         | Title                            | File                                                                                                                    | Type            |
| :------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :-------------- |
| **00-10-06-000** | CS-25 Requirements Trace Matrix  | [GP-AM-AMPEL-0100-53-00-10-60-000-XML-A.xml](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-60/GP-AM-AMPEL-0100-53-00-10-60-000-XML-A.xml)   | XML, REQ, IDX |
| **00-10-06-001** | CS-25 Compliance Strategy Desc | [GP-AM-AMPEL-0100-53-00-10-60-001-MD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-60/GP-AM-AMPEL-0100-53-00-10-60-001-MD-A.md)    | MD, PLAN        |

##### 00‑10‑07 — S1000D BREX File Generation <a name="ata‑00‑10‑07"></a>

| Doc ID         | Title                           | File                                                                                                                    | Type         |
| :------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------------------------- | :----------- |
| **00-10-07-000** | Project BREX File (S1000D)      | [GP-AM-AMPEL-0100-53-00-10-70-000-XML-A.xml](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-70/GP-AM-AMPEL-0100-53-00-10-70-000-XML-A.xml)   | XML, SPEC    |
| **00-10-07-001** | BREX Generation Tool Desc     | [GP-AM-AMPEL-0100-53-00-10-70-001-SDD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-70/GP-AM-AMPEL-0100-53-00-10-70-001-SDD-A.md)    | SDD          |

##### 00‑10‑08 — Controlled Glossary Integration <a name="ata‑00‑10‑08"></a>

| Doc ID         | Title                                | File                                                                                                                    | Type         |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------- |
| **00-10-08-000** | Ref to Master Controlled Glossary    | [GP-AM-AMPEL-0100-53-00-10-80-000-REF-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-80/GP-AM-AMPEL-0100-53-00-10-80-000-REF-A.md)   | REF, GLO     |
| **00-10-08-001** | Glossary Term Contribution Proc    | [GP-AM-AMPEL-0100-53-00-10-80-001-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-80/GP-AM-AMPEL-0100-53-00-10-80-001-PROC-A.md) | PROC         |

##### 00‑10‑09 — Reporting and Auditability System <a name="ata‑00‑10‑09"></a>

| Doc ID         | Title                            | File                                                                                                                    | Type   |
| :------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **00-10-09-000** | Reporting & Auditability Sys Desc| [GP-AM-AMPEL-0100-53-00-10-90-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-90/GP-AM-AMPEL-0100-53-00-10-90-000-SDD-A.md) | SDD    |
| **00-10-09-001** | Example Audit Trail Report       | [GP-AM-AMPEL-0100-53-00-10-90-001-RPT-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-10/00-90/GP-AM-AMPEL-0100-53-00-10-90-001-RPT-A.md) | RPT    |

#### 00‑20‑00 — Standard Practices <a name="ata‑00‑20‑00"></a>

| Doc ID         | Title                 | File                                                                                                          | Type   |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-20-00-000** | Standard Procedures   | [GP-AM-AMPEL-0100-53-00-20-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-20/GP-AM-AMPEL-0100-53-00-20-000-PROC-A.md) | PROC   |
| **00-20-10-000** | Safety Procedures     | [GP-AM-AMPEL-0100-53-00-20-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-20/GP-AM-AMPEL-0100-53-00-20-10-000-PROC-A.md) | PROC   |

#### 00‑30‑00 — Dimensions & Areas <a name="ata‑00‑30‑00"></a>

| Doc ID         | Title                  | File                                                                                                          | Type   |
| :------------- | :--------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-30-00-000** | Aircraft Dimensions    | [GP-AM-AMPEL-0100-53-00-30-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-30/GP-AM-AMPEL-0100-53-00-30-000-LIST-A.md) | LIST   |
| **00-30-00-001** | Dimensional Drawings   | [GP-AM-AMPEL-0100-53-00-30-001-DWG-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-30/GP-AM-AMPEL-0100-53-00-30-001-DWG-A.md)  | DWG    |

#### 00‑40‑00 — Lifting and Shoring <a name="ata‑00‑40‑00"></a>

| Doc ID         | Title                       | File                                                                                                          | Type   |
| :------------- | :-------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-40-00-000** | Lifting Procedures          | [GP-AM-AMPEL-0100-53-00-40-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-40/GP-AM-AMPEL-0100-53-00-40-000-PROC-A.md) | PROC   |
| **00-40-00-001** | Lifting Points & Equipment| [GP-AM-AMPEL-0100-53-00-40-001-DWG-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-40/GP-AM-AMPEL-0100-53-00-40-001-DWG-A.md)  | DWG    |

#### 00‑50‑00 — Leveling and Weighing <a name="ata‑00‑50‑00"></a>

| Doc ID         | Title                 | File                                                                                                          | Type   |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-50-00-000** | Leveling Procedures   | [GP-AM-AMPEL-0100-53-00-50-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-50/GP-AM-AMPEL-0100-53-00-50-000-PROC-A.md) | PROC   |
| **00-50-10-000** | Weighing Procedures   | [GP-AM-AMPEL-0100-53-00-50-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-50/GP-AM-AMPEL-0100-53-00-50-10-000-PROC-A.md) | PROC   |

#### 00‑60‑00 — Ground Handling and Servicing <a name="ata‑00‑60‑00"></a>

| Doc ID         | Title                       | File                                                                                                          | Type   |
| :------------- | :-------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-60-00-000** | Ground Handling Procedures  | [GP-AM-AMPEL-0100-53-00-60-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-60/GP-AM-AMPEL-0100-53-00-60-000-PROC-A.md) | PROC   |
| **00-60-10-000** | Servicing Procedures        | [GP-AM-AMPEL-0100-53-00-60-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-60/GP-AM-AMPEL-0100-53-00-60-10-000-PROC-A.md) | PROC   |

#### 00‑70‑00 — Standard Practices - Engines <a name="ata‑00‑70‑00"></a>

| Doc ID         | Title                                | File                                                                                                          | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-70-00-000** | Engine Maintenance Practices       | [GP-AM-AMPEL-0100-53-00-70-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-70/GP-AM-AMPEL-0100-53-00-70-000-PROC-A.md) | PROC   |
| **00-70-00-001** | Engine Interface Control (Ref ATA 71)| [GP-AM-AMPEL-0100-53-00-70-001-ICD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-70/GP-AM-AMPEL-0100-53-00-70-001-ICD-A.md)  | ICD    |

#### 00‑80‑00 — Standard Practices - Systems <a name="ata‑00‑80‑00"></a>

| Doc ID         | Title                               | File                                                                                                          | Type   |
| :------------- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-80-00-000** | Systems Maintenance Practices     | [GP-AM-AMPEL-0100-53-00-80-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-80/GP-AM-AMPEL-0100-53-00-80-000-PROC-A.md) | PROC   |
| **00-80-10-000** | Electrical Practices (Ref ATA 20) | [GP-AM-AMPEL-0100-53-00-80-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-80/GP-AM-AMPEL-0100-53-00-80-10-000-PROC-A.md) | PROC   |

#### 00‑90‑00 — Integration with GAIA AIR Systems <a name="ata‑00‑90‑00"></a>

| Doc ID         | Title                                | File                                                                                                          | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **00-90-00-000** | GAIA AIR Integration               | [GP-AM-AMPEL-0100-53-00-90-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-90/GP-AM-AMPEL-0100-53-00-90-000-ICD-A.md)  | ICD    |
| **00-90-10-000** | BITT Integration (Ref GP-COM-BITT) | [GP-AM-AMPEL-0100-53-00-90-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA00_General/00-90/GP-AM-AMPEL-0100-53-00-90-10-000-ICD-A.md) | ICD    |

---

### ATA 01 — Aircraft General <a name="ata‑01"></a>

#### 01‑10‑00 — Aircraft Identification <a name="ata‑01‑10‑00"></a>

| Doc ID   | Title                | File     | Type   |
| :------- | :------------------- | :------- | :----- |
| *(TBD)* | *(To Be Determined)* | *(N/A)* | *(N/A)* |

#### 01‑20‑00 — Principal Characteristics <a name="ata‑01‑20‑00"></a>

| Doc ID   | Title                             | File     | Type   |
| :------- | :-------------------------------- | :------- | :----- |
| *(TBD)* | *(References ATA 00-30, 06, 08)* | *(N/A)* | *(N/A)* |

#### 01‑30‑00 — General Arrangement <a name="ata‑01‑30‑00"></a>

| Doc ID   | Title                              | File     | Type   |
| :------- | :--------------------------------- | :------- | :----- |
| *(TBD)* | *(References ATA 00-10-Std, 06)* | *(N/A)* | *(N/A)* |

---

### ATA 02 — Operations Information <a name="ata‑02"></a>

#### 02‑10‑00 — Flight Manual / Pilot Operating Handbook <a name="ata‑02‑10‑00"></a>

| Doc ID   | Title                        | File     | Type   |
| :------- | :--------------------------- | :------- | :----- |
| *(TBD)* | *(Link to AFM/POH Document)* | *(N/A)* | *(N/A)* |

#### 02‑20‑00 — Standard Operating Procedures (SOP) <a name="ata‑02‑20‑00"></a>

| Doc ID   | Title                    | File     | Type   |
| :------- | :----------------------- | :------- | :----- |
| *(TBD)* | *(Link to SOP Document)* | *(N/A)* | *(N/A)* |

#### 02‑30‑00 — AI-Assisted Flight Planning Information <a name="ata‑02‑30‑00"></a>

| Doc ID         | Title                                     | File                                                                                                          | Type   |
| :------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **02-30-00-000** | AI Flight Planning Tool Desc (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-02-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA02_Operations/02-30/GP-AM-AMPEL-0100-53-02-30-00-000-SDD-A.md) | SDD    |

---

### ATA 03 — Performance <a name="ata‑03"></a>

#### 03‑10‑00 — Takeoff and Landing Performance <a name="ata‑03‑10‑00"></a>

| Doc ID   | Title                       | File     | Type   |
| :------- | :-------------------------- | :------- | :----- |
| *(TBD)* | *(Performance Data/Charts)* | *(N/A)* | *(N/A)* |

#### 03‑20‑00 — Climb Performance <a name="ata‑03‑20‑00"></a>

| Doc ID   | Title                       | File     | Type   |
| :------- | :-------------------------- | :------- | :----- |
| *(TBD)* | *(Performance Data/Charts)* | *(N/A)* | *(N/A)* |

#### 03‑30‑00 — Cruise Performance <a name="ata‑03‑30‑00"></a>

| Doc ID   | Title                       | File     | Type   |
| :------- | :-------------------------- | :------- | :----- |
| *(TBD)* | *(Performance Data/Charts)* | *(N/A)* | *(N/A)* |

#### 03‑40‑00 — Descent Performance <a name="ata‑03‑40‑00"></a>

| Doc ID   | Title                       | File     | Type   |
| :------- | :-------------------------- | :------- | :----- |
| *(TBD)* | *(Performance Data/Charts)* | *(N/A)* | *(N/A)* |

#### 03‑50‑00 — Performance Monitoring Systems <a name="ata‑03‑50‑00"></a>

| Doc ID         | Title                                           | File                                                                                                          | Type   |
| :------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **03-50-00-000** | Perf Mon Sys Desc (Ref ATA 31, GP-COM-AI) | [GP-AM-AMPEL-0100-53-03-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA03_Performance/03-50/GP-AM-AMPEL-0100-53-03-50-00-000-SDD-A.md) | SDD    |

---

### ATA 04 — Airworthiness <a name="ata‑04"></a>

#### 04‑10‑00 — Certification Basis <a name="ata‑04‑10‑00"></a>

| Doc ID   | Title                                | File     | Type   |
| :------- | :----------------------------------- | :------- | :----- |
| *(TBD)* | *(Link to TCDS/Certification Plan)* | *(N/A)* | *(N/A)* |

#### 04‑20‑00 — Airworthiness Limitations <a name="ata‑04‑20‑00"></a>

| Doc ID   | Title                     | File     | Type   |
| :------- | :------------------------ | :------- | :----- |
| *(TBD)* | *(Link to ALS Section)* | *(N/A)* | *(N/A)* |

#### 04‑30‑00 — MMEL / CDL <a name="ata‑04‑30‑00"></a>

| Doc ID   | Title                       | File     | Type   |
| :------- | :-------------------------- | :------- | :----- |
| *(TBD)* | *(Link to MMEL/CDL Docs)* | *(N/A)* | *(N/A)* |

#### 04‑40‑00 — Continued Airworthiness Management <a name="ata‑04‑40‑00"></a>

| Doc ID   | Title                            | File     | Type   |
| :------- | :------------------------------- | :------- | :----- |
| *(TBD)* | *(Link to CAME/Maint Prog Ov.)* | *(N/A)* | *(N/A)* |

---

### ATA 05 — Time Limits/Maintenance Checks <a name="ata‑05"></a>

#### 05‑00‑00 — General <a name="ata‑05‑00‑00"></a>

| Doc ID         | Title                              | File                                                                                                          | Type   |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **05-00-00-000** | Time Limits Overview               | [GP-AM-AMPEL-0100-53-05-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-00/GP-AM-AMPEL-0100-53-05-00-00-000-OV-A.md)   | OV     |
| **05-00-00-001** | Maintenance Program Specifications | [GP-AM-AMPEL-0100-53-05-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-00/GP-AM-AMPEL-0100-53-05-00-00-001-SPEC-A.md)| SPEC   |

#### 05‑10‑00 — Time Limits <a name="ata‑05‑10‑00"></a>

| Doc ID         | Title                 | File                                                                                                            | Type   |
| :------------- | :-------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **05-10-00-000** | Component Time Limits | [GP-AM-AMPEL-0100-53-05-10-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-10/GP-AM-AMPEL-0100-53-05-10-00-000-LIST-A.md)| LIST   |
| **05-10-10-000** | Life-Limited Parts    | [GP-AM-AMPEL-0100-53-05-10-10-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-10/GP-AM-AMPEL-0100-53-05-10-10-000-LIST-A.md)| LIST   |

#### 05‑20‑00 — Scheduled Maintenance Checks <a name="ata‑05‑20‑00"></a>

| Doc ID         | Title                         | File                                                                                                            | Type   |
| :------------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **05-20-00-000** | Maintenance Planning Document | [GP-AM-AMPEL-0100-53-05-20-00-000-MPD-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-20/GP-AM-AMPEL-0100-53-05-20-00-000-MPD-A.md)   | MPD    |
| **05-20-10-000** | A-Check Procedures            | [GP-AM-AMPEL-0100-53-05-20-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-20/GP-AM-AMPEL-0100-53-05-20-10-000-PROC-A.md)| PROC   |
| **05-20-20-000** | C-Check Procedures            | [GP-AM-AMPEL-0100-53-05-20-20-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-20/GP-AM-AMPEL-0100-53-05-20-20-000-PROC-A.md)| PROC   |

#### 05‑30‑00 — Unscheduled Maintenance Checks <a name="ata‑05‑30‑00"></a>

| Doc ID         | Title                         | File                                                                                                            | Type   |
| :------------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **05-30-00-000** | Special Inspection Procedures | [GP-AM-AMPEL-0100-53-05-30-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-30/GP-AM-AMPEL-0100-53-05-30-00-000-PROC-A.md)| PROC   |
| **05-30-10-000** | Hard Landing Inspection       | [GP-AM-AMPEL-0100-53-05-30-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-30/GP-AM-AMPEL-0100-53-05-30-10-000-PROC-A.md)| PROC   |

#### 05‑40‑00 — BITT-Enhanced Maintenance <a name="ata‑05‑40‑00"></a>

| Doc ID         | Title                               | File                                                                                                            | Type   |
| :------------- | :---------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **05-40-00-000** | Blockchain-Based Maint. Tracking  | [GP-AM-AMPEL-0100-53-05-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-40/GP-AM-AMPEL-0100-53-05-40-00-000-SDD-A.md)   | SDD    |
| **05-40-10-000** | BITT Maintenance Int (Ref GP-COM-BITT)| [GP-AM-AMPEL-0100-53-05-40-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-40/GP-AM-AMPEL-0100-53-05-40-10-000-ICD-A.md)  | ICD    |

#### 05‑50‑00 — Predictive Maintenance <a name="ata‑05‑50‑00"></a>

| Doc ID         | Title                                  | File                                                                                                            | Type   |
| :------------- | :------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **05-50-00-000** | AI-Driven Predictive Maintenance     | [GP-AM-AMPEL-0100-53-05-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-50/GP-AM-AMPEL-0100-53-05-50-00-000-SDD-A.md)   | SDD    |
| **05-50-10-000** | i-Aher0 Maintenance Int (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-05-50-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA05_TimeLimits/05-50/GP-AM-AMPEL-0100-53-05-50-10-000-ICD-A.md)  | ICD    |

---

### ATA 06 — Dimensions and Areas <a name="ata‑06"></a>

#### 06‑00‑00 — General <a name="ata‑06‑00‑00"></a>

| Doc ID         | Title                 | File                                                                                                      | Type   |
| :------------- | :-------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **06-00-00-000** | Dimensions Overview   | [GP-AM-AMPEL-0100-53-06-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-00/GP-AM-AMPEL-0100-53-06-00-00-000-OV-A.md) | OV     |
| **06-00-00-001** | Principal Dimensions  | [GP-AM-AMPEL-0100-53-06-00-00-001-DWG-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-00/GP-AM-AMPEL-0100-53-06-00-00-001-DWG-A.md)| DWG    |

#### 06‑10‑00 — Aircraft Zones and Stations <a name="ata‑06‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                        | Type   |
| :------------- | :------------------------ | :---------------------------------------------------------------------------------------------------------- | :----- |
| **06-10-00-000** | Zone Diagram              | [GP-AM-AMPEL-0100-53-06-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-10/GP-AM-AMPEL-0100-53-06-10-00-000-DWG-A.md) | DWG    |
| **06-10-10-000** | Station Numbering System  | [GP-AM-AMPEL-0100-53-06-10-10-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-10/GP-AM-AMPEL-0100-53-06-10-10-000-LIST-A.md)| LIST   |

#### 06‑20‑00 — Access Doors and Panels <a name="ata‑06‑20‑00"></a>

| Doc ID         | Title                   | File                                                                                                        | Type   |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **06-20-00-000** | Access Door Locations   | [GP-AM-AMPEL-0100-53-06-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-20/GP-AM-AMPEL-0100-53-06-20-00-000-DWG-A.md) | DWG    |
| **06-20-10-000** | Access Panel Index      | [GP-AM-AMPEL-0100-53-06-20-10-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-20/GP-AM-AMPEL-0100-53-06-20-10-000-LIST-A.md)| LIST   |

#### 06‑30‑00 — Zonal Inspection Requirements <a name="ata‑06‑30‑00"></a>

| Doc ID         | Title                         | File                                                                                                          | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **06-30-00-000** | Zonal Inspection Procedures   | [GP-AM-AMPEL-0100-53-06-30-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-30/GP-AM-AMPEL-0100-53-06-30-00-000-PROC-A.md)| PROC   |
| **06-30-10-000** | Zonal Inspection Requirements | [GP-AM-AMPEL-0100-53-06-30-10-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-30/GP-AM-AMPEL-0100-53-06-30-10-000-LIST-A.md)| LIST   |

#### 06‑40‑00 — Digital Twin Integration <a name="ata‑06‑40‑00"></a>

| Doc ID         | Title                             | File                                                                                                          | Type   |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **06-40-00-000** | Digital Twin Interface            | [GP-AM-AMPEL-0100-53-06-40-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-40/GP-AM-AMPEL-0100-53-06-40-00-000-ICD-A.md)  | ICD    |
| **06-40-10-000** | 3D Model Int (Ref GP-COM-DTO) | [GP-AM-AMPEL-0100-53-06-40-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA06_Dimensions/06-40/GP-AM-AMPEL-0100-53-06-40-10-000-SDD-A.md)  | SDD    |

---

*(Continuing for all chapters 07-99 in the same format...)*

---
### ATA 07 — Lifting and Shoring <a name="ata‑07"></a>

#### 07‑00‑00 — General <a name="ata‑07‑00‑00"></a>

| Doc ID         | Title                          | File                                                                                                    | Type   |
| :------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------ | :----- |
| **07-00-00-000** | Lifting and Shoring Overview | [GP-AM-AMPEL-0100-53-07-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-00/GP-AM-AMPEL-0100-53-07-00-00-000-OV-A.md)   | OV     |
| **07-00-00-001** | Lifting Equipment Specs    | [GP-AM-AMPEL-0100-53-07-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-00/GP-AM-AMPEL-0100-53-07-00-00-001-SPEC-A.md)| SPEC   |

#### 07‑10‑00 — Jacking <a name="ata‑07‑10‑00"></a>

| Doc ID         | Title              | File                                                                                                        | Type   |
| :------------- | :----------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **07-10-00-000** | Jacking Procedures | [GP-AM-AMPEL-0100-53-07-10-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-10/GP-AM-AMPEL-0100-53-07-10-00-000-PROC-A.md)| PROC   |
| **07-10-10-000** | Jacking Points     | [GP-AM-AMPEL-0100-53-07-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-10/GP-AM-AMPEL-0100-53-07-10-10-000-DWG-A.md)  | DWG    |

#### 07‑20‑00 — Shoring <a name="ata‑07‑20‑00"></a>

| Doc ID         | Title              | File                                                                                                        | Type   |
| :------------- | :----------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **07-20-00-000** | Shoring Procedures | [GP-AM-AMPEL-0100-53-07-20-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-20/GP-AM-AMPEL-0100-53-07-20-00-000-PROC-A.md)| PROC   |
| **07-20-10-000** | Shoring Points     | [GP-AM-AMPEL-0100-53-07-20-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-20/GP-AM-AMPEL-0100-53-07-20-10-000-DWG-A.md)  | DWG    |

#### 07‑30‑00 — Hoisting <a name="ata‑07‑30‑00"></a>

| Doc ID         | Title              | File                                                                                                        | Type   |
| :------------- | :----------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **07-30-00-000** | Hoisting Procedures| [GP-AM-AMPEL-0100-53-07-30-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-30/GP-AM-AMPEL-0100-53-07-30-00-000-PROC-A.md)| PROC   |
| **07-30-10-000** | Hoisting Points    | [GP-AM-AMPEL-0100-53-07-30-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-30/GP-AM-AMPEL-0100-53-07-30-10-000-DWG-A.md)  | DWG    |

#### 07‑40‑00 — Robotic Lifting Integration <a name="ata‑07‑40‑00"></a>

| Doc ID         | Title                               | File                                                                                                        | Type   |
| :------------- | :---------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **07-40-00-000** | Robotic Lifting Int (Ref GP-RAME) | [GP-AM-AMPEL-0100-53-07-40-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-40/GP-AM-AMPEL-0100-53-07-40-00-000-ICD-A.md)  | ICD    |
| **07-40-10-000** | Automated Lifting Procedures      | [GP-AM-AMPEL-0100-53-07-40-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA07_Lifting/07-40/GP-AM-AMPEL-0100-53-07-40-10-000-PROC-A.md)| PROC   |

---
### ATA 08 — Leveling and Weighing <a name="ata‑08"></a>

#### 08‑00‑00 — General <a name="ata‑08‑00‑00"></a>

| Doc ID         | Title                         | File                                                                                                        | Type   |
| :------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **08-00-00-000** | Leveling and Weighing Overview| [GP-AM-AMPEL-0100-53-08-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-00/GP-AM-AMPEL-0100-53-08-00-00-000-OV-A.md)   | OV     |
| **08-00-00-001** | Equipment Specifications      | [GP-AM-AMPEL-0100-53-08-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-00/GP-AM-AMPEL-0100-53-08-00-00-001-SPEC-A.md)| SPEC   |

#### 08‑10‑00 — Leveling <a name="ata‑08‑10‑00"></a>

| Doc ID         | Title               | File                                                                                                        | Type   |
| :------------- | :------------------ | :---------------------------------------------------------------------------------------------------------- | :----- |
| **08-10-00-000** | Leveling Procedures | [GP-AM-AMPEL-0100-53-08-10-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-10/GP-AM-AMPEL-0100-53-08-10-00-000-PROC-A.md)| PROC   |
| **08-10-10-000** | Leveling Points     | [GP-AM-AMPEL-0100-53-08-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-10/GP-AM-AMPEL-0100-53-08-10-10-000-DWG-A.md)  | DWG    |

#### 08‑20‑00 — Weighing <a name="ata‑08‑20‑00"></a>

| Doc ID         | Title               | File                                                                                                        | Type   |
| :------------- | :------------------ | :---------------------------------------------------------------------------------------------------------- | :----- |
| **08-20-00-000** | Weighing Procedures | [GP-AM-AMPEL-0100-53-08-20-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-20/GP-AM-AMPEL-0100-53-08-20-00-000-PROC-A.md)| PROC   |
| **08-20-10-000** | Weight Calculations | [GP-AM-AMPEL-0100-53-08-20-10-000-CAL-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-20/GP-AM-AMPEL-0100-53-08-20-10-000-CAL-A.md)  | CAL    |

#### 08‑30‑00 — Weight and Balance <a name="ata‑08‑30‑00"></a>

| Doc ID         | Title                          | File                                                                                                        | Type   |
| :------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **08-30-00-000** | Center of Gravity Calculations | [GP-AM-AMPEL-0100-53-08-30-00-000-CAL-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-30/GP-AM-AMPEL-0100-53-08-30-00-000-CAL-A.md)  | CAL    |
| **08-30-10-000** | Weight and Balance Control     | [GP-AM-AMPEL-0100-53-08-30-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-30/GP-AM-AMPEL-0100-53-08-30-10-000-PROC-A.md)| PROC   |

#### 08‑40‑00 — Digital Weight Management <a name="ata‑08‑40‑00"></a>

| Doc ID         | Title                                | File                                                                                                        | Type   |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **08-40-00-000** | Digital Weight and Balance System  | [GP-AM-AMPEL-0100-53-08-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-40/GP-AM-AMPEL-0100-53-08-40-00-000-SDD-A.md)  | SDD    |
| **08-40-10-000** | Weight Data Int (Ref GP-COM-BITT)| [GP-AM-AMPEL-0100-53-08-40-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA08_Leveling/08-40/GP-AM-AMPEL-0100-53-08-40-10-000-ICD-A.md)  | ICD    |

---
### ATA 09 — Towing and Taxiing <a name="ata‑09"></a>

#### 09‑00‑00 — General <a name="ata‑09‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                      | Type   |
| :------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **09-00-00-000** | Towing and Taxiing Overview | [GP-AM-AMPEL-0100-53-09-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-00/GP-AM-AMPEL-0100-53-09-00-00-000-OV-A.md)   | OV     |
| **09-00-00-001** | Equipment Specifications    | [GP-AM-AMPEL-0100-53-09-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-00/GP-AM-AMPEL-0100-53-09-00-00-001-SPEC-A.md)| SPEC   |

#### 09‑10‑00 — Towing <a name="ata‑09‑10‑00"></a>

| Doc ID         | Title                   | File                                                                                                      | Type   |
| :------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **09-10-00-000** | Towing Procedures       | [GP-AM-AMPEL-0100-53-09-10-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-10/GP-AM-AMPEL-0100-53-09-10-00-000-PROC-A.md)| PROC   |
| **09-10-10-000** | Towing Attachment Points| [GP-AM-AMPEL-0100-53-09-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-10/GP-AM-AMPEL-0100-53-09-10-10-000-DWG-A.md)  | DWG    |

#### 09‑20‑00 — Taxiing <a name="ata‑09‑20‑00"></a>

| Doc ID         | Title               | File                                                                                                      | Type   |
| :------------- | :------------------ | :-------------------------------------------------------------------------------------------------------- | :----- |
| **09-20-00-000** | Taxiing Procedures  | [GP-AM-AMPEL-0100-53-09-20-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-20/GP-AM-AMPEL-0100-53-09-20-00-000-PROC-A.md)| PROC   |
| **09-20-10-000** | Emergency Taxiing   | [GP-AM-AMPEL-0100-53-09-20-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-20/GP-AM-AMPEL-0100-53-09-20-10-000-PROC-A.md)| PROC   |

#### 09‑30‑00 — Autonomous Ground Movement <a name="ata‑09‑30‑00"></a>

| Doc ID         | Title                                 | File                                                                                                      | Type   |
| :------------- | :------------------------------------ | :-------------------------------------------------------------------------------------------------------- | :----- |
| **09-30-00-000** | Autonomous Taxiing System           | [GP-AM-AMPEL-0100-53-09-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-30/GP-AM-AMPEL-0100-53-09-30-00-000-SDD-A.md)  | SDD    |
| **09-30-10-000** | Ground Movement AI Int (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-09-30-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-30/GP-AM-AMPEL-0100-53-09-30-10-000-ICD-A.md)  | ICD    |

#### 09‑40‑00 — Ground Traffic Management <a name="ata‑09‑40‑00"></a>

| Doc ID         | Title                                   | File                                                                                                      | Type   |
| :------------- | :-------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **09-40-00-000** | Ground Traffic Management Int (Ref GP-GRO)| [GP-AM-AMPEL-0100-53-09-40-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-40/GP-AM-AMPEL-0100-53-09-40-00-000-ICD-A.md)  | ICD    |
| **09-40-10-000** | Coordinated Movement Procedures       | [GP-AM-AMPEL-0100-53-09-40-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA09_Towing/09-40/GP-AM-AMPEL-0100-53-09-40-10-000-PROC-A.md)| PROC   |

---
### ATA 10 — Parking, Mooring, Storage and Return to Service <a name="ata‑10"></a>

#### 10‑00‑00 — General <a name="ata‑10‑00‑00"></a>

| Doc ID         | Title                         | File                                                                                                          | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **10-00-00-000** | Parking and Storage Overview  | [GP-AM-AMPEL-0100-53-10-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-00/GP-AM-AMPEL-0100-53-10-00-00-000-OV-A.md)   | OV     |
| **10-00-00-001** | Equipment Specifications      | [GP-AM-AMPEL-0100-53-10-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-00/GP-AM-AMPEL-0100-53-10-00-00-001-SPEC-A.md)| SPEC   |

#### 10‑10‑00 — Parking and Mooring <a name="ata‑10‑10‑00"></a>

| Doc ID         | Title              | File                                                                                                          | Type   |
| :------------- | :----------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **10-10-00-000** | Parking Procedures | [GP-AM-AMPEL-0100-53-10-10-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-10/GP-AM-AMPEL-0100-53-10-10-00-000-PROC-A.md)| PROC   |
| **10-10-10-000** | Mooring Procedures | [GP-AM-AMPEL-0100-53-10-10-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-10/GP-AM-AMPEL-0100-53-10-10-10-000-PROC-A.md)| PROC   |

#### 10‑20‑00 — Storage <a name="ata‑10‑20‑00"></a>

| Doc ID         | Title              | File                                                                                                          | Type   |
| :------------- | :----------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **10-20-00-000** | Short-Term Storage | [GP-AM-AMPEL-0100-53-10-20-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-20/GP-AM-AMPEL-0100-53-10-20-00-000-PROC-A.md)| PROC   |
| **10-20-10-000** | Long-Term Storage  | [GP-AM-AMPEL-0100-53-10-20-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-20/GP-AM-AMPEL-0100-53-10-20-10-000-PROC-A.md)| PROC   |

#### 10‑30‑00 — Return to Service <a name="ata‑10‑30‑00"></a>

| Doc ID         | Title                     | File                                                                                                          | Type   |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------ | :----- |
| **10-30-00-000** | Reactivation Procedures   | [GP-AM-AMPEL-0100-53-10-30-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-30/GP-AM-AMPEL-0100-53-10-30-00-000-PROC-A.md)| PROC   |
| **10-30-10-000** | Return to Service Testing | [GP-AM-AMPEL-0100-53-10-30-10-000-TEST-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-30/GP-AM-AMPEL-0100-53-10-30-10-000-TEST-A.md)| TEST   |

#### 10‑40‑00 — Digital Storage Management <a name="ata‑10‑40‑00"></a>

| Doc ID         | Title                                | File                                                                                                          | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **10-40-00-000** | Digital Storage Monitoring         | [GP-AM-AMPEL-0100-53-10-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-40/GP-AM-AMPEL-0100-53-10-40-00-000-SDD-A.md)  | SDD    |
| **10-40-10-000** | Storage Data Int (Ref GP-COM-BITT)| [GP-AM-AMPEL-0100-53-10-40-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA10_Parking/10-40/GP-AM-AMPEL-0100-53-10-40-10-000-ICD-A.md)  | ICD    |

---
### ATA 11 — Placards and Markings <a name="ata‑11"></a>

#### 11‑00‑00 — General <a name="ata‑11‑00‑00"></a>

| Doc ID         | Title                           | File                                                                                                            | Type   |
| :------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **11-00-00-000** | Placards and Markings Overview  | [GP-AM-AMPEL-0100-53-11-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-00/GP-AM-AMPEL-0100-53-11-00-00-000-OV-A.md)   | OV     |
| **11-00-00-001** | Marking Standards and Specs     | [GP-AM-AMPEL-0100-53-11-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-00/GP-AM-AMPEL-0100-53-11-00-00-001-SPEC-A.md)| SPEC   |

#### 11‑10‑00 — Exterior Markings <a name="ata‑11‑10‑00"></a>

| Doc ID         | Title                              | File                                                                                                            | Type   |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **11-10-00-000** | Exterior Markings Index            | [GP-AM-AMPEL-0100-53-11-10-00-000-IDX-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-10/GP-AM-AMPEL-0100-53-11-10-00-000-IDX-A.md)   | IDX    |
| **11-10-10-000** | Registration and Livery Drawings   | [GP-AM-AMPEL-0100-53-11-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-10/GP-AM-AMPEL-0100-53-11-10-10-000-DWG-A.md)   | DWG    |
| **11-10-20-000** | Exterior Warning Markings Spec   | [GP-AM-AMPEL-0100-53-11-10-20-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-10/GP-AM-AMPEL-0100-53-11-10-20-000-SPEC-A.md)| SPEC   |

#### 11‑20‑00 — Interior Placards <a name="ata‑11‑20‑00"></a>

| Doc ID         | Title                       | File                                                                                                            | Type   |
| :------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **11-20-00-000** | Interior Placards Index     | [GP-AM-AMPEL-0100-53-11-20-00-000-IDX-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-20/GP-AM-AMPEL-0100-53-11-20-00-000-IDX-A.md)   | IDX    |
| **11-20-10-000** | Cockpit Placard Locations   | [GP-AM-AMPEL-0100-53-11-20-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-20/GP-AM-AMPEL-0100-53-11-20-10-000-DWG-A.md)   | DWG    |
| **11-20-20-000** | Cabin Placard List          | [GP-AM-AMPEL-0100-53-11-20-20-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-20/GP-AM-AMPEL-0100-53-11-20-20-000-LIST-A.md)| LIST   |

#### 11‑30‑00 — Special Markings <a name="ata‑11‑30‑00"></a>

| Doc ID         | Title                                     | File                                                                                                            | Type   |
| :------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **11-30-00-000** | High-Voltage System Markings (Ref ATA 24) | [GP-AM-AMPEL-0100-53-11-30-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-30/GP-AM-AMPEL-0100-53-11-30-00-000-SPEC-A.md)| SPEC   |
| **11-30-10-000** | Quantum System Markings (Ref ATA 72-Q01)  | [GP-AM-AMPEL-0100-53-11-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA11_Placards/11-30/GP-AM-AMPEL-0100-53-11-30-10-000-SPEC-A.md)| SPEC   |

---
### ATA 12 — Servicing <a name="ata‑12"></a>

#### 12‑00‑00 — General <a name="ata‑12‑00‑00"></a>

| Doc ID         | Title                     | File                                                                                                          | Type       |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------ | :--------- |
| **12-00-00-000** | Servicing Overview        | [GP-AM-AMPEL-0100-53-12-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-00/GP-AM-AMPEL-0100-53-12-00-00-000-OV-A.md)   | OV         |
| **12-00-00-001** | Consumables Specification | [GP-AM-AMPEL-0100-53-12-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-00/GP-AM-AMPEL-0100-53-12-00-00-001-SPEC-A.md)| SPEC, LIST |

#### 12‑10‑00 — Fuel Servicing <a name="ata‑12‑10‑00"></a>

| Doc ID         | Title                                | File                                                                                                          | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-10-00-000** | Fueling Procedure (H2/SAF) (Ref ATA 28) | [GP-AM-AMPEL-0100-53-12-10-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-10/GP-AM-AMPEL-0100-53-12-10-00-000-PROC-A.md)| PROC   |
| **12-10-10-000** | Defueling Procedure (H2/SAF)       | [GP-AM-AMPEL-0100-53-12-10-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-10/GP-AM-AMPEL-0100-53-12-10-10-000-PROC-A.md)| PROC   |

#### 12‑20‑00 — Oil Servicing <a name="ata‑12‑20‑00"></a>

| Doc ID         | Title                           | File                                                                                                          | Type   |
| :------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-20-00-000** | Engine Oil Servicing (Ref ATA 79)| [GP-AM-AMPEL-0100-53-12-20-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-20/GP-AM-AMPEL-0100-53-12-20-00-000-PROC-A.md)| PROC   |

#### 12‑30‑00 — Hydraulic Fluid Servicing <a name="ata‑12‑30‑00"></a>

| Doc ID         | Title                         | File                                                                                                          | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-30-00-000** | EHA Fluid Servicing (Ref ATA 13)| [GP-AM-AMPEL-0100-53-12-30-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-30/GP-AM-AMPEL-0100-53-12-30-00-000-PROC-A.md)| PROC   |

#### 12‑40‑00 — Pneumatic and Oxygen Servicing <a name="ata‑12‑40‑00"></a>

| Doc ID         | Title                             | File                                                                                                          | Type   |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-40-00-000** | Oxygen System Servicing (Ref ATA 35)| [GP-AM-AMPEL-0100-53-12-40-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-40/GP-AM-AMPEL-0100-53-12-40-00-000-PROC-A.md)| PROC   |

#### 12‑50‑00 — Other Fluid Servicing <a name="ata‑12‑50‑00"></a>

| Doc ID         | Title                                         | File                                                                                                          | Type   |
| :------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-50-00-000** | Water/Waste Servicing (Ref ATA 38)            | [GP-AM-AMPEL-0100-53-12-50-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-50/GP-AM-AMPEL-0100-53-12-50-00-000-PROC-A.md)| PROC   |
| **12-50-10-000** | Quantum System Coolant Servicing (Ref ATA 72-Q01)| [GP-AM-AMPEL-0100-53-12-50-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-50/GP-AM-AMPEL-0100-53-12-50-10-000-PROC-A.md)| PROC   |

#### 12‑60‑00 — Cleaning <a name="ata‑12‑60‑00"></a>

| Doc ID         | Title             | File                                                                                                          | Type   |
| :------------- | :---------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-60-00-000** | Exterior Cleaning | [GP-AM-AMPEL-0100-53-12-60-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-60/GP-AM-AMPEL-0100-53-12-60-00-000-PROC-A.md)| PROC   |
| **12-60-10-000** | Interior Cleaning | [GP-AM-AMPEL-0100-53-12-60-10-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-60/GP-AM-AMPEL-0100-53-12-60-10-000-PROC-A.md)| PROC   |

#### 12‑70‑00 — Automated Servicing Integration <a name="ata‑12‑70‑00"></a>

| Doc ID         | Title                                     | File                                                                                                          | Type   |
| :------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **12-70-00-000** | Robotic Servicing Int Desc (Ref GP-RAME)| [GP-AM-AMPEL-0100-53-12-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-70/GP-AM-AMPEL-0100-53-12-70-00-000-SDD-A.md)  | SDD    |
| **12-70-10-000** | Automated Servicing Port Interface      | [GP-AM-AMPEL-0100-53-12-70-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA12_Servicing/12-70/GP-AM-AMPEL-0100-53-12-70-10-000-ICD-A.md)  | ICD    |

---
### ATA 13 — Hydraulic Power (Minimal/EHA) <a name="ata‑13"></a>

#### 13‑00‑00 — General <a name="ata‑13‑00‑00"></a>

| Doc ID         | Title                             | File                                                                                                            | Type     |
| :------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **13-00-00-000** | Hydraulic Sys Ov (Minimal/EHA)  | [GP-AM-AMPEL-0100-53-13-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-00/GP-AM-AMPEL-0100-53-13-00-00-000-OV-A.md)     | OV, SDD  |
| **13-00-00-001** | System Specification            | [GP-AM-AMPEL-0100-53-13-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-00/GP-AM-AMPEL-0100-53-13-00-00-001-SPEC-A.md) | SPEC     |

#### 13‑10‑00 — Electro-Hydrostatic Actuation (EHA) <a name="ata‑13‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                            | Type     |
| :------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **13-10-00-000** | EHA Unit Design           | [GP-AM-AMPEL-0100-53-13-10-00-000-DD-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-10/GP-AM-AMPEL-0100-53-13-10-00-000-DD-A.md)     | DD, DWG  |
| **13-10-10-000** | EHA Performance Spec    | [GP-AM-AMPEL-0100-53-13-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-10/GP-AM-AMPEL-0100-53-13-10-10-000-SPEC-A.md)| SPEC     |
| **13-10-20-000** | EHA Maintenance Manual    | [GP-AM-AMPEL-0100-53-13-10-20-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-10/GP-AM-AMPEL-0100-53-13-10-20-000-MAN-A.md)  | MAN      |

#### 13‑20‑00 — Hydraulic Lines and Fittings <a name="ata‑13‑20‑00"></a>

| Doc ID         | Title                              | File                                                                                                            | Type   |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **13-20-00-000** | Hydraulic Line Routing (Redundancy)| [GP-AM-AMPEL-0100-53-13-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-20/GP-AM-AMPEL-0100-53-13-20-00-000-DWG-A.md) | DWG    |
| **13-20-10-000** | Fitting Specifications           | [GP-AM-AMPEL-0100-53-13-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-20/GP-AM-AMPEL-0100-53-13-20-10-000-SPEC-A.md)| SPEC   |

#### 13‑30‑00 — System Monitoring <a name="ata‑13‑30‑00"></a>

| Doc ID         | Title                     | File                                                                                                            | Type   |
| :------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **13-30-00-000** | Monitoring System Desc    | [GP-AM-AMPEL-0100-53-13-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-30/GP-AM-AMPEL-0100-53-13-30-00-000-SDD-A.md)  | SDD    |
| **13-30-10-000** | Sensor Specifications     | [GP-AM-AMPEL-0100-53-13-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA13_Hydraulic/13-30/GP-AM-AMPEL-0100-53-13-30-10-000-SPEC-A.md)| SPEC   |

---
### ATA 14 — Pneumatic Power (Minimal) <a name="ata‑14"></a>

#### 14‑00‑00 — General <a name="ata‑14‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                            | Type     |
| :------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **14-00-00-000** | Pneumatic Sys Ov (Minimal)| [GP-AM-AMPEL-0100-53-14-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-00/GP-AM-AMPEL-0100-53-14-00-00-000-OV-A.md)     | OV, SDD  |
| **14-00-00-001** | System Specification      | [GP-AM-AMPEL-0100-53-14-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-00/GP-AM-AMPEL-0100-53-14-00-00-001-SPEC-A.md) | SPEC     |

#### 14‑10‑00 — Bleed Air System <a name="ata‑14‑10‑00"></a>

| Doc ID         | Title                              | File                                                                                                            | Type   |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **14-10-00-000** | Bleed Air Distribution (Ref ATA 36)| [GP-AM-AMPEL-0100-53-14-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-10/GP-AM-AMPEL-0100-53-14-10-00-000-SDD-A.md)  | SDD    |
| **14-10-10-000** | Bleed Air Ducting Drawing        | [GP-AM-AMPEL-0100-53-14-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-10/GP-AM-AMPEL-0100-53-14-10-10-000-DWG-A.md)  | DWG    |

#### 14‑20‑00 — Auxiliary Pneumatic Sources <a name="ata‑14‑20‑00"></a>

| Doc ID         | Title                             | File                                                                                                            | Type   |
| :------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **14-20-00-000** | Electric Compressor Design      | [GP-AM-AMPEL-0100-53-14-20-00-000-DD-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-20/GP-AM-AMPEL-0100-53-14-20-00-000-DD-A.md)     | DD     |
| **14-20-10-000** | Electric Compressor Spec (Ref ATA 36)| [GP-AM-AMPEL-0100-53-14-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-20/GP-AM-AMPEL-0100-53-14-20-10-000-SPEC-A.md)| SPEC   |

#### 14‑30‑00 — System Monitoring <a name="ata‑14‑30‑00"></a>

| Doc ID         | Title                     | File                                                                                                            | Type   |
| :------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **14-30-00-000** | Monitoring System Desc    | [GP-AM-AMPEL-0100-53-14-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-30/GP-AM-AMPEL-0100-53-14-30-00-000-SDD-A.md)  | SDD    |
| **14-30-10-000** | Sensor Specifications     | [GP-AM-AMPEL-0100-53-14-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA14_Pneumatic/14-30/GP-AM-AMPEL-0100-53-14-30-10-000-SPEC-A.md)| SPEC   |

---
### ATA 15 — Air Conditioning <a name="ata‑15"></a>

#### 15‑00‑00 — General <a name="ata‑15‑00‑00"></a>

| Doc ID         | Title                 | File                                                                                                      | Type   |
| :------------- | :-------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **15-00-00-000** | Reference to ATA 21 | [GP-AM-AMPEL-0100-53-15-00-00-000-REF-A.md](./GP-AM/AMPEL_0100/ATA15_AirCond/15-00/GP-AM-AMPEL-0100-53-15-00-00-000-REF-A.md) | REF    |

---
### ATA 16 — Pressurization <a name="ata‑16"></a>

#### 16‑00‑00 — General <a name="ata‑16‑00‑00"></a>

| Doc ID         | Title                 | File                                                                                                          | Type   |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **16-00-00-000** | Reference to ATA 21 | [GP-AM-AMPEL-0100-53-16-00-00-000-REF-A.md](./GP-AM/AMPEL_0100/ATA16_Pressuriz/16-00/GP-AM-AMPEL-0100-53-16-00-00-000-REF-A.md) | REF    |

---
### ATA 17 — Environmental Control <a name="ata‑17"></a>

#### 17‑00‑00 — General <a name="ata‑17‑00‑00"></a>

| Doc ID         | Title                 | File                                                                                                      | Type   |
| :------------- | :-------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **17-00-00-000** | Reference to ATA 21 | [GP-AM-AMPEL-0100-53-17-00-00-000-REF-A.md](./GP-AM/AMPEL_0100/ATA17_EnvCtrl/17-00/GP-AM-AMPEL-0100-53-17-00-00-000-REF-A.md) | REF    |

---
### ATA 18 — Vibration and Noise Control <a name="ata‑18"></a>

#### 18‑00‑00 — General <a name="ata‑18‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                              | Type     |
| :------------- | :-------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **18-00-00-000** | Vibration and Noise Overview| [GP-AM-AMPEL-0100-53-18-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-00/GP-AM-AMPEL-0100-53-18-00-00-000-OV-A.md)     | OV       |
| **18-00-00-001** | Limits and Requirements     | [GP-AM-AMPEL-0100-53-18-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-00/GP-AM-AMPEL-0100-53-18-00-00-001-SPEC-A.md) | SPEC, REQ|

#### 18‑10‑00 — Vibration Monitoring System <a name="ata‑18‑10‑00"></a>

| Doc ID         | Title                                      | File                                                                                                              | Type     |
| :------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **18-10-00-000** | HUMS Description                           | [GP-AM-AMPEL-0100-53-18-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-10/GP-AM-AMPEL-0100-53-18-10-00-000-SDD-A.md)    | SDD      |
| **18-10-10-000** | Sensor Specifications                    | [GP-AM-AMPEL-0100-53-18-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-10/GP-AM-AMPEL-0100-53-18-10-10-000-SPEC-A.md) | SPEC     |
| **18-10-20-000** | AI Anomaly Detection Algo (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-18-10-20-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-10/GP-AM-AMPEL-0100-53-18-10-20-000-ALGO-A.md) | ALGO, SDD|

#### 18‑20‑00 — Noise Control <a name="ata‑18‑20‑00"></a>

| Doc ID         | Title                              | File                                                                                                              | Type     |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **18-20-00-000** | Active Noise Cancellation System   | [GP-AM-AMPEL-0100-53-18-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-20/GP-AM-AMPEL-0100-53-18-20-00-000-SDD-A.md)    | SDD      |
| **18-20-10-000** | Acoustic Liner Specifications    | [GP-AM-AMPEL-0100-53-18-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-20/GP-AM-AMPEL-0100-53-18-20-10-000-SPEC-A.md) | SPEC     |
| **18-20-20-000** | Noise Measurement Test Report    | [GP-AM-AMPEL-0100-53-18-20-20-000-TEST-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-20/GP-AM-AMPEL-0100-53-18-20-20-000-TEST-A.md) | TEST, RPT|

#### 18‑30‑00 — Noise Reduction Technologies (NR) <a name="ata‑18‑30‑00"></a>

| Doc ID         | Title                                          | File                                                                                                              | Type   |
| :------------- | :--------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **18-30-00-000** | Noise Reduction Technologies Overview          | [GP-AM-AMPEL-0100-53-18-30-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-30/GP-AM-AMPEL-0100-53-18-30-00-000-OV-A.md)     | OV     |
| **18-30-10-000** | Landing Gear Noise Reduction Design (Ref ATA 32)| [GP-AM-AMPEL-0100-53-18-30-10-000-DD-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-30/GP-AM-AMPEL-0100-53-18-30-10-000-DD-A.md)      | DD     |
| **18-30-20-000** | Engine Nozzle Noise Opt Design (Ref ATA 78)  | [GP-AM-AMPEL-0100-53-18-30-20-000-DD-A.md](./GP-AM/AMPEL_0100/ATA18_Vibration/18-30/GP-AM-AMPEL-0100-53-18-30-20-000-DD-A.md)      | DD     |

---
### ATA 20 — Standard Practices - Airframe <a name="ata‑20"></a>

#### 20‑00‑00 — General Standard Practices <a name="ata‑20‑00‑00‑std"></a>

| Doc ID         | Title                         | File                                                                                                              | Type   |
| :------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **20-00-00-000** | Standard Practices Overview   | [GP-AM-AMPEL-0100-53-20-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/20-00/GP-AM-AMPEL-0100-53-20-00-00-000-OV-A.md)   | OV     |
| **20-00-00-001** | General Standards             | [GP-AM-AMPEL-0100-53-20-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/20-00/GP-AM-AMPEL-0100-53-20-00-00-001-SPEC-A.md)| SPEC   |

#### 20‑10‑00 — Sustainable Materials Standards <a name="ata‑20‑10‑00‑std"></a>

| Doc ID         | Title                                  | File                                                                                                              | Type   |
| :------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **20-10-00-000** | Sustainable Material Specs (Ref GP-SUPL)| [GP-AM-AMPEL-0100-53-20-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/20-10/GP-AM-AMPEL-0100-53-20-10-00-000-SPEC-A.md)| SPEC   |
| **20-10-10-000** | Bio-based Composite Standards          | [GP-AM-AMPEL-0100-53-20-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/20-10/GP-AM-AMPEL-0100-53-20-10-10-000-SPEC-A.md)| SPEC   |

#### 20‑20‑00 — Green Manufacturing Processes <a name="ata‑20‑20‑00‑std"></a>

| Doc ID         | Title                                  | File                                                                                                              | Type   |
| :------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **20-20-00-000** | Green Manufacturing Procs (Ref GP-SUPL)| [GP-AM-AMPEL-0100-53-20-20-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/20-20/GP-AM-AMPEL-0100-53-20-20-00-000-PROC-A.md)| PROC   |

#### 20‑30‑00 — Sustainable Repair Procedures <a name="ata‑20‑30‑00‑std"></a>

| Doc ID         | Title                                       | File                                                                                                              | Type   |
| :------------- | :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **20-30-00-000** | BNNT/Carbon-Lattice Repair Proc (Ref ATA 51)| [GP-AM-AMPEL-0100-53-20-30-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/20-30/GP-AM-AMPEL-0100-53-20-30-00-000-PROC-A.md)| PROC   |

#### AM — Advanced Manufacturing Technologies <a name="ata‑20‑am"></a>

##### AM‑10 — Additive Manufacturing <a name="ata‑20‑am‑10"></a>

| Doc ID       | Title                             | File                                                                                                          | Type   |
| :----------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **AM-10-000**  | Additive Manufacturing Overview | [GP-AM-AMPEL-0100-53-20-AM10-000-OV-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/AM-10/GP-AM-AMPEL-0100-53-20-AM10-000-OV-A.md)    | OV     |
| **AM-10-10-000** | Large-Scale Printing Spec       | [GP-AM-AMPEL-0100-53-20-AM10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/AM-10/GP-AM-AMPEL-0100-53-20-AM10-10-000-SPEC-A.md)| SPEC   |

##### AM‑20 — Automated Fiber Placement <a name="ata‑20‑am‑20"></a>

| Doc ID       | Title                              | File                                                                                                         | Type   |
| :----------- | :--------------------------------- | :----------------------------------------------------------------------------------------------------------- | :----- |
| **AM-20-000**  | Automated Fiber Placement Overview | [GP-AM-AMPEL-0100-53-20-AM20-000-OV-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/AM-20/GP-AM-AMPEL-0100-53-20-AM20-000-OV-A.md) | OV     |

##### AM‑30 — Out-of-Autoclave Processing <a name="ata‑20‑am‑30"></a>

| Doc ID       | Title                               | File                                                                                                         | Type   |
| :----------- | :---------------------------------- | :----------------------------------------------------------------------------------------------------------- | :----- |
| **AM-30-000**  | Out-of-Autoclave Processing Overview| [GP-AM-AMPEL-0100-53-20-AM30-000-OV-A.md](./GP-AM/AMPEL_0100/ATA20_StdPractices/AM-30/GP-AM-AMPEL-0100-53-20-AM30-000-OV-A.md) | OV     |

---
### ATA 21 — Air Conditioning and Pressurization (ECS) <a name="ata‑21"></a>

#### 21‑00‑00 — General <a name="ata‑21‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                            | Type     |
| :------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **21-00-00-000** | ECS Overview            | [GP-AM-AMPEL-0100-53-21-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-00/GP-AM-AMPEL-0100-53-21-00-00-000-OV-A.md)       | OV, SDD  |
| **21-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-21-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-00/GP-AM-AMPEL-0100-53-21-00-00-001-SPEC-A.md) | SPEC     |

#### 21‑10‑00 — Air Supply <a name="ata‑21‑10‑00"></a>

| Doc ID         | Title                                   | File                                                                                                            | Type   |
| :------------- | :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **21-10-00-000** | Air Source Desc (Bleed/Elec)(Ref ATA 36)| [GP-AM-AMPEL-0100-53-21-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-10/GP-AM-AMPEL-0100-53-21-10-00-000-SDD-A.md)  | SDD    |

#### 21‑20‑00 — Air Distribution <a name="ata‑21‑20‑00"></a>

| Doc ID         | Title                           | File                                                                                                            | Type     |
| :------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **21-20-00-000** | Cabin Air Distribution Diagram  | [GP-AM-AMPEL-0100-53-21-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-20/GP-AM-AMPEL-0100-53-21-20-00-000-DWG-A.md)  | DWG, FIG |
| **21-20-10-000** | Filtration System Spec        | [GP-AM-AMPEL-0100-53-21-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-20/GP-AM-AMPEL-0100-53-21-20-10-000-SPEC-A.md)| SPEC     |

#### 21‑30‑00 — Pressurization Control <a name="ata‑21‑30‑00"></a>

| Doc ID         | Title                          | File                                                                                                            | Type   |
| :------------- | :----------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **21-30-00-000** | Pressurization Control Sys Desc| [GP-AM-AMPEL-0100-53-21-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-30/GP-AM-AMPEL-0100-53-21-30-00-000-SDD-A.md)  | SDD    |
| **21-30-10-000** | Outflow Valve Specification    | [GP-AM-AMPEL-0100-53-21-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-30/GP-AM-AMPEL-0100-53-21-30-10-000-SPEC-A.md)| SPEC   |

#### 21‑50‑00 — Air Conditioning Packs <a name="ata‑21‑50‑00"></a>

| Doc ID         | Title                | File                                                                                                            | Type   |
| :------------- | :------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **21-50-00-000** | Green ECS Technology | [GP-AM-AMPEL-0100-53-21-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-50/GP-AM-AMPEL-0100-53-21-50-00-000-SDD-A.md)  | SDD    |

#### 21‑60‑00 — AI-Driven ECS <a name="ata‑21‑60‑00"></a>

| Doc ID         | Title                                     | File                                                                                                            | Type     |
| :------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **21-60-00-000** | AI Personalized Climate Zones             | [GP-AM-AMPEL-0100-53-21-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-60/GP-AM-AMPEL-0100-53-21-60-00-000-SDD-A.md)    | SDD      |
| **21-60-10-000** | Optimization Algorithms (Ref GP-COM-AI) | [GP-AM-AMPEL-0100-53-21-60-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA21_ECS/21-60/GP-AM-AMPEL-0100-53-21-60-10-000-ALGO-A.md) | ALGO, SDD|

---
### ATA 22 — Auto Flight <a name="ata‑22"></a>

#### 22‑00‑00 — General <a name="ata‑22‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                                | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **22-00-00-000** | Auto Flight Overview    | [GP-AM-AMPEL-0100-53-22-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-00/GP-AM-AMPEL-0100-53-22-00-00-000-OV-A.md)     | OV, SDD  |
| **22-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-22-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-00/GP-AM-AMPEL-0100-53-22-00-00-001-SPEC-A.md) | SPEC     |

#### 22‑10‑00 — Autopilot <a name="ata‑22‑10‑00"></a>

| Doc ID         | Title                                       | File                                                                                                                | Type     |
| :------------- | :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **22-10-00-000** | Autopilot Architecture                      | [GP-AM-AMPEL-0100-53-22-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-10/GP-AM-AMPEL-0100-53-22-10-00-000-SDD-A.md)   | SDD, FIG |
| **22-10-10-000** | AI Autopilot Algorithms (Ref GP-COM-AI)     | [GP-AM-AMPEL-0100-53-22-10-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-10/GP-AM-AMPEL-0100-53-22-10-10-000-ALGO-A.md) | ALGO, SDD|
| **22-10-20-000** | Quantum-Enhanced Control Logic (Ref GP-COM-QAO)| [GP-AM-AMPEL-0100-53-22-10-20-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-10/GP-AM-AMPEL-0100-53-22-10-20-000-ALGO-A.md) | ALGO, SDD|

#### 22‑20‑00 — Flight Management System (FMS) <a name="ata‑22‑20‑00"></a>

| Doc ID         | Title                                        | File                                                                                                                | Type     |
| :------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **22-20-00-000** | FMS Description                              | [GP-AM-AMPEL-0100-53-22-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-20/GP-AM-AMPEL-0100-53-22-20-00-000-SDD-A.md)   | SDD      |
| **22-20-10-000** | AI Route Optimization Algos (Ref GP-COM-AI)  | [GP-AM-AMPEL-0100-53-22-20-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-20/GP-AM-AMPEL-0100-53-22-20-10-000-ALGO-A.md) | ALGO, SDD|
| **22-20-20-000** | FMS to QAO Interface (Ref GP-COM-QAO)      | [GP-AM-AMPEL-0100-53-22-20-20-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-20/GP-AM-AMPEL-0100-53-22-20-20-000-ICD-A.md)    | ICD      |

#### 22‑30‑00 — Auto Throttle <a name="ata‑22‑30‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                | Type   |
| :------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **22-30-00-000** | Auto Throttle System Description        | [GP-AM-AMPEL-0100-53-22-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-30/GP-AM-AMPEL-0100-53-22-30-00-000-SDD-A.md)  | SDD    |
| **22-30-10-000** | Fuel Efficiency Algorithms (Ref ATA 73) | [GP-AM-AMPEL-0100-53-22-30-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA22_Autoflight/22-30/GP-AM-AMPEL-0100-53-22-30-10-000-ALGO-A.md)| ALGO   |

---
### ATA 23 — Communications <a name="ata‑23"></a>

#### 23‑00‑00 — General <a name="ata‑23‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                      | Type     |
| :------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------- | :------- |
| **23-00-00-000** | Communications Overview | [GP-AM-AMPEL-0100-53-23-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-00/GP-AM-AMPEL-0100-53-23-00-00-000-OV-A.md)       | OV, SDD  |
| **23-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-23-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-00/GP-AM-AMPEL-0100-53-23-00-00-001-SPEC-A.md) | SPEC     |

#### 23‑10‑00 — Speech Communication <a name="ata‑23‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                      | Type   |
| :------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------- | :----- |
| **23-10-00-000** | VHF/HF/SATCOM Description | [GP-AM-AMPEL-0100-53-23-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-10/GP-AM-AMPEL-0100-53-23-10-00-000-SDD-A.md)  | SDD    |
| **23-10-10-000** | Transceiver Specs       | [GP-AM-AMPEL-0100-53-23-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-10/GP-AM-AMPEL-0100-53-23-10-10-000-SPEC-A.md)| SPEC   |

#### 23‑20‑00 — Data Link Communication <a name="ata‑23‑20‑00"></a>

| Doc ID         | Title                           | File                                                                                                      | Type   |
| :------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------- | :----- |
| **23-20-00-000** | ACARS/ATC Data Link Description | [GP-AM-AMPEL-0100-53-23-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-20/GP-AM-AMPEL-0100-53-23-20-00-000-SDD-A.md)  | SDD    |
| **23-20-10-000** | Protocol Specifications       | [GP-AM-AMPEL-0100-53-23-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-20/GP-AM-AMPEL-0100-53-23-20-10-000-SPEC-A.md)| SPEC   |

#### 23‑50‑00 — Audio Integrating System <a name="ata‑23‑50‑00"></a>

| Doc ID         | Title                | File                                                                                                      | Type   |
| :------------- | :------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **23-50-00-000** | Intercom/PA System   | [GP-AM-AMPEL-0100-53-23-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-50/GP-AM-AMPEL-0100-53-23-50-00-000-SDD-A.md)  | SDD    |

#### 23‑70‑00 — AI Communications Management <a name="ata‑23‑70‑00"></a>

| Doc ID         | Title                                      | File                                                                                                      | Type   |
| :------------- | :----------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **23-70-00-000** | AI Management Function (Ref GP-COM-AI)     | [GP-AM-AMPEL-0100-53-23-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-70/GP-AM-AMPEL-0100-53-23-70-00-000-SDD-A.md)    | SDD    |
| **23-70-10-000** | AI Spectrum Optimization Algorithm       | [GP-AM-AMPEL-0100-53-23-70-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-70/GP-AM-AMPEL-0100-53-23-70-10-000-ALGO-A.md) | ALGO   |

#### 23‑80‑00 — Quantum Key Distribution (QKD) <a name="ata‑23‑80‑00"></a>

| Doc ID         | Title                               | File                                                                                                      | Type   |
| :------------- | :---------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **23-80-00-000** | QKD System Integration (Ref GP-COM-QAO)| [GP-AM-AMPEL-0100-53-23-80-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-80/GP-AM-AMPEL-0100-53-23-80-00-000-SDD-A.md)    | SDD    |
| **23-80-10-000** | Secure Protocol Specifications    | [GP-AM-AMPEL-0100-53-23-80-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA23_Comms/23-80/GP-AM-AMPEL-0100-53-23-80-10-000-SPEC-A.md) | SPEC   |

---
### ATA 24 — Electrical Power <a name="ata‑24"></a>

#### 24‑00‑00 — General <a name="ata‑24‑00‑00"></a>

| Doc ID         | Title                    | File                                                                                                              | Type     |
| :------------- | :----------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **24-00-00-000** | Electrical System Overview | [GP-AM-AMPEL-0100-53-24-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-00/GP-AM-AMPEL-0100-53-24-00-00-000-OV-A.md)   | OV, SDD  |
| **24-00-00-001** | System Specifications    | [GP-AM-AMPEL-0100-53-24-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-00/GP-AM-AMPEL-0100-53-24-00-00-001-SPEC-A.md)| SPEC     |

#### 24‑20‑00 — AC Generation <a name="ata‑24‑20‑00"></a>

| Doc ID         | Title                         | File                                                                                                              | Type   |
| :------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **24-20-00-000** | AC Generation System Description| [GP-AM-AMPEL-0100-53-24-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-20/GP-AM-AMPEL-0100-53-24-20-00-000-SDD-A.md)  | SDD    |

#### 24‑30‑00 — DC Generation <a name="ata‑24‑30‑00"></a>

| Doc ID         | Title                                | File                                                                                                              | Type   |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **24-30-00-000** | DC Generation Sys Desc (TRU/Battery)| [GP-AM-AMPEL-0100-53-24-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-30/GP-AM-AMPEL-0100-53-24-30-00-000-SDD-A.md)  | SDD    |
| **24-30-10-000** | Battery System Specification       | [GP-AM-AMPEL-0100-53-24-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-30/GP-AM-AMPEL-0100-53-24-30-10-000-SPEC-A.md)| SPEC   |

#### 24‑40‑00 — External Power <a name="ata‑24‑40‑00"></a>

| Doc ID         | Title                  | File                                                                                                              | Type     |
| :------------- | :--------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **24-40-00-000** | Ground Power Interface | [GP-AM-AMPEL-0100-53-24-40-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-40/GP-AM-AMPEL-0100-53-24-40-00-000-ICD-A.md)    | ICD, SPEC|

#### 24‑50‑00 — Distribution <a name="ata‑24‑50‑00"></a>

| Doc ID         | Title                                    | File                                                                                                              | Type     |
| :------------- | :--------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **24-50-00-000** | Load Distribution Architecture         | [GP-AM-AMPEL-0100-53-24-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-50/GP-AM-AMPEL-0100-53-24-50-00-000-SDD-A.md)  | SDD, DWG |
| **24-50-10-000** | AI Load Management Algo (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-24-50-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-50/GP-AM-AMPEL-0100-53-24-50-10-000-ALGO-A.md)| ALGO, SDD|

#### 24‑60‑00 — Integrated Power Systems <a name="ata‑24‑60‑00"></a>

| Doc ID         | Title                     | File                                                                                                              | Type   |
| :------------- | :------------------------ | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **24-60-00-000** | AEHCS System Description  | [GP-AM-AMPEL-0100-53-24-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA24_Electrical/24-60/GP-AM-AMPEL-0100-53-24-60-00-000-SDD-A.md)  | SDD    |

---
### ATA 25 — Equipment and Furnishings <a name="ata‑25"></a>

#### 25‑00‑00 — General <a name="ata‑25‑00‑00"></a>

| Doc ID         | Title                           | File                                                                                                                | Type     |
| :------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **25-00-00-000** | Equipment & Furnishings Ov    | [GP-AM-AMPEL-0100-53-25-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-00/GP-AM-AMPEL-0100-53-25-00-00-000-OV-A.md)     | OV       |
| **25-00-00-001** | Standards and Requirements    | [GP-AM-AMPEL-0100-53-25-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-00/GP-AM-AMPEL-0100-53-25-00-00-001-SPEC-A.md) | SPEC, REQ|

#### 25‑10‑00 — Flight Compartment <a name="ata‑25‑10‑00"></a>


| **25-10-00-000** | Crew Seat Specification | [GP-AM-AMPEL-0100-53-25-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-10/GP-AM-AMPEL-0100-53-25-10-00-000-SPEC-A.md)| SPEC   |

#### 25‑20‑00 — Passenger Compartment <a name="ata‑25‑20‑00"></a>

| Doc ID         | Title                                  | File                                                                                                                | Type       |
| :------------- | :------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :--------- |
| **25-20-00-000** | Cabin Layout Design                  | [GP-AM-AMPEL-0100-53-25-20-00-000-DD-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-20/GP-AM-AMPEL-0100-53-25-20-00-000-DD-A.md)      | DD, FIG    |
| **25-20-10-000** | Passenger Seat Specification         | [GP-AM-AMPEL-0100-53-25-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-20/GP-AM-AMPEL-0100-53-25-20-10-000-SPEC-A.md) | SPEC       |
| **25-20-20-000** | VR Window System Desc (Ref ATA 44, 56) | [GP-AM-AMPEL-0100-53-25-20-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-20/GP-AM-AMPEL-0100-53-25-20-20-000-SDD-A.md)   | SDD        |
| **25-20-30-000** | Sustainable Interior Materials List  | [GP-AM-AMPEL-0100-53-25-20-30-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-20/GP-AM-AMPEL-0100-53-25-20-30-000-LIST-A.md) | LIST, SPEC |

#### 25‑40‑00 — Cargo Compartment <a name="ata‑25‑40‑00"></a>

| Doc ID         | Title                                 | File                                                                                                                | Type   |
| :------------- | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **25-40-00-000** | Cargo Loading System Desc (Ref ATA 50)| [GP-AM-AMPEL-0100-53-25-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-40/GP-AM-AMPEL-0100-53-25-40-00-000-SDD-A.md)  | SDD    |

#### 25‑50‑00 — Galley <a name="ata‑25‑50‑00"></a>

| Doc ID         | Title                 | File                                                                                                                | Type       |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------ | :--------- |
| **25-50-00-000** | Galley Equipment List | [GP-AM-AMPEL-0100-53-25-50-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-50/GP-AM-AMPEL-0100-53-25-50-00-000-LIST-A.md)| LIST, SPEC |

Okay, Comandante. Correcting the last entry for ATA 25 and continuing with the breakdown for ATA 26 through 99 using the established 4-column Markdown table format.

---

#### 25‑60‑00 — Emergency Equipment <a name="ata‑25‑60‑00"></a>

| Doc ID         | Title                    | File                                                                                                                  | Type   |
| :------------- | :----------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----- |
| **25-60-00-000** | Emergency Equipment List | [GP-AM-AMPEL-0100-53-25-60-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-60/GP-AM-AMPEL-0100-53-25-60-00-000-LIST-A.md)| LIST   |
| **25-60-10-000** | Location Drawing         | [GP-AM-AMPEL-0100-53-25-60-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA25_Furnishings/25-60/GP-AM-AMPEL-0100-53-25-60-10-000-DWG-A.md)  | DWG    |

---
### ATA 26 — Fire Protection <a name="ata‑26"></a>

#### 26‑00‑00 — General <a name="ata‑26‑00‑00"></a>

| Doc ID         | Title                      | File                                                                                                                    | Type     |
| :------------- | :------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------- |
| **26-00-00-000** | Fire Protection Overview | [GP-AM-AMPEL-0100-53-26-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-00/GP-AM-AMPEL-0100-53-26-00-00-000-OV-A.md)   | OV, SDD  |
| **26-00-00-001** | System Specifications    | [GP-AM-AMPEL-0100-53-26-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-00/GP-AM-AMPEL-0100-53-26-00-00-001-SPEC-A.md)| SPEC     |

#### 26‑10‑00 — Detection <a name="ata‑26‑10‑00"></a>

| Doc ID         | Title                                         | File                                                                                                                    | Type     |
| :------------- | :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------- |
| **26-10-00-000** | Detector Specifications                   | [GP-AM-AMPEL-0100-53-26-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-10/GP-AM-AMPEL-0100-53-26-10-00-000-SPEC-A.md)| SPEC     |
| **26-10-10-000** | Detector Locations                        | [GP-AM-AMPEL-0100-53-26-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-10/GP-AM-AMPEL-0100-53-26-10-10-000-DWG-A.md)  | DWG      |
| **26-10-20-000** | AI Detection Algos (H2/Battery)(Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-26-10-20-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-10/GP-AM-AMPEL-0100-53-26-10-20-000-ALGO-A.md)| ALGO, SDD|

#### 26‑20‑00 — Extinguishing <a name="ata‑26‑20‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                    | Type   |
| :------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **26-20-00-000** | Extinguisher Sys Desc (Halon Alt.)    | [GP-AM-AMPEL-0100-53-26-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-20/GP-AM-AMPEL-0100-53-26-20-00-000-SDD-A.md)    | SDD    |
| **26-20-10-000** | Agent Specifications                  | [GP-AM-AMPEL-0100-53-26-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-20/GP-AM-AMPEL-0100-53-26-20-10-000-SPEC-A.md) | SPEC   |
| **26-20-20-000** | Zone-Specific Systems (Engine/APU/Cargo)| [GP-AM-AMPEL-0100-53-26-20-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA26_FireProtection/26-20/GP-AM-AMPEL-0100-53-26-20-20-000-SDD-A.md)    | SDD    |

---
### ATA 27 — Flight Controls <a name="ata‑27"></a>

#### 27‑00‑00 — General <a name="ata‑27‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                                    | Type     |
| :------------- | :-------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------- |
| **27-00-00-000** | Flight Control System Ov  | [GP-AM-AMPEL-0100-53-27-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-00/GP-AM-AMPEL-0100-53-27-00-00-000-OV-A.md)     | OV, SDD, FIG |
| **27-00-00-001** | System Specifications     | [GP-AM-AMPEL-0100-53-27-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-00/GP-AM-AMPEL-0100-53-27-00-00-001-SPEC-A.md) | SPEC     |

#### 27‑10‑00 — Aileron <a name="ata‑27‑10‑00"></a>

| Doc ID         | Title                                  | File                                                                                                                    | Type   |
| :------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-10-00-000** | Aileron System Description           | [GP-AM-AMPEL-0100-53-27-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-10/GP-AM-AMPEL-0100-53-27-10-00-000-SDD-A.md)  | SDD    |
| **27-10-10-000** | Actuation Specification (Ref ATA 13/29)| [GP-AM-AMPEL-0100-53-27-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-10/GP-AM-AMPEL-0100-53-27-10-10-000-SPEC-A.md)| SPEC   |

#### 27‑20‑00 — Rudder <a name="ata‑27‑20‑00"></a>

| Doc ID         | Title                                  | File                                                                                                                    | Type   |
| :------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-20-00-000** | Rudder System Description (Ref ATA 55) | [GP-AM-AMPEL-0100-53-27-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-20/GP-AM-AMPEL-0100-53-27-20-00-000-SDD-A.md)  | SDD    |
| **27-20-10-000** | Actuation Specification              | [GP-AM-AMPEL-0100-53-27-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-20/GP-AM-AMPEL-0100-53-27-20-10-000-SPEC-A.md)| SPEC   |

#### 27‑30‑00 — Elevator <a name="ata‑27‑30‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                    | Type   |
| :------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-30-00-000** | Elevator System Description (Ref ATA 55)| [GP-AM-AMPEL-0100-53-27-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-30/GP-AM-AMPEL-0100-53-27-30-00-000-SDD-A.md)  | SDD    |
| **27-30-10-000** | Actuation Specification               | [GP-AM-AMPEL-0100-53-27-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-30/GP-AM-AMPEL-0100-53-27-30-10-000-SPEC-A.md)| SPEC   |

#### 27‑40‑00 — Stabilizer Trim <a name="ata‑27‑40‑00"></a>

| Doc ID         | Title                                      | File                                                                                                                    | Type   |
| :------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-40-00-000** | Stabilizer Trim System Desc (Ref ATA 55) | [GP-AM-AMPEL-0100-53-27-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-40/GP-AM-AMPEL-0100-53-27-40-00-000-SDD-A.md)  | SDD    |

#### 27‑50‑00 — Flaps <a name="ata‑27‑50‑00"></a>

| Doc ID         | Title                                | File                                                                                                                    | Type   |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-50-00-000** | Flap System Description (Ref ATA 57) | [GP-AM-AMPEL-0100-53-27-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-50/GP-AM-AMPEL-0100-53-27-50-00-000-SDD-A.md)  | SDD    |
| **27-50-10-000** | Actuation Specification            | [GP-AM-AMPEL-0100-53-27-50-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-50/GP-AM-AMPEL-0100-53-27-50-10-000-SPEC-A.md)| SPEC   |

#### 27‑60‑00 — Spoilers <a name="ata‑27‑60‑00"></a>

| Doc ID         | Title                                  | File                                                                                                                    | Type   |
| :------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-60-00-000** | Spoiler System Description (Ref ATA 57)| [GP-AM-AMPEL-0100-53-27-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-60/GP-AM-AMPEL-0100-53-27-60-00-000-SDD-A.md)  | SDD    |
| **27-60-10-000** | Actuation Specification              | [GP-AM-AMPEL-0100-53-27-60-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-60/GP-AM-AMPEL-0100-53-27-60-10-000-SPEC-A.md)| SPEC   |

#### 27‑80‑00 — Slats <a name="ata‑27‑80‑00"></a>

| Doc ID         | Title                                | File                                                                                                                    | Type   |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **27-80-00-000** | Slat System Description (Ref ATA 57) | [GP-AM-AMPEL-0100-53-27-80-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-80/GP-AM-AMPEL-0100-53-27-80-00-000-SDD-A.md)  | SDD    |
| **27-80-10-000** | Actuation Specification            | [GP-AM-AMPEL-0100-53-27-80-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-80/GP-AM-AMPEL-0100-53-27-80-10-000-SPEC-A.md)| SPEC   |

#### 27‑90‑00 — GPAM (GAIA Polymorphic Aero-Morphing) <a name="ata‑27‑90‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                    | Type     |
| :------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------- |
| **27-90-00-000** | GPAM System Overview (Ref ATA 57)     | [GP-AM-AMPEL-0100-53-27-90-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-90/GP-AM-AMPEL-0100-53-27-90-00-000-OV-A.md)      | OV, SDD  |
| **27-90-10-000** | Control Logic Algos (Ref GP-COM-AI)   | [GP-AM-AMPEL-0100-53-27-90-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-90/GP-AM-AMPEL-0100-53-27-90-10-000-ALGO-A.md) | ALGO, SDD|
| **27-90-20-000** | GPAM Actuation Int (Ref ATA 13/29)  | [GP-AM-AMPEL-0100-53-27-90-20-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA27_FlightControls/27-90/GP-AM-AMPEL-0100-53-27-90-20-000-ICD-A.md)    | ICD      |

---
### ATA 28 — Fuel (Hybrid H2/SAF) <a name="ata‑28"></a>

#### 28‑00‑00 — General <a name="ata‑28‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                  | Type     |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **28-00-00-000** | Fuel System Overview    | [GP-AM-AMPEL-0100-53-28-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-00/GP-AM-AMPEL-0100-53-28-00-00-000-OV-A.md)       | OV, SDD, FIG |
| **28-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-28-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-00/GP-AM-AMPEL-0100-53-28-00-00-001-SPEC-A.md) | SPEC     |

#### 28‑10‑00 — Storage <a name="ata‑28‑10‑00"></a>

| Doc ID         | Title                            | File                                                                                                  | Type     |
| :------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **28-10-00-000** | Cryogenic Hydrogen Tank Design | [GP-AM-AMPEL-0100-53-28-10-00-000-DD-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-10/GP-AM-AMPEL-0100-53-28-10-00-000-DD-A.md)     | DD, DWG  |
| **28-10-10-000** | Cryogenic Hydrogen Tank Spec   | [GP-AM-AMPEL-0100-53-28-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-10/GP-AM-AMPEL-0100-53-28-10-10-000-SPEC-A.md)| SPEC     |
| **28-10-20-000** | SAF Tank Design                | [GP-AM-AMPEL-0100-53-28-10-20-000-DD-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-10/GP-AM-AMPEL-0100-53-28-10-20-000-DD-A.md)     | DD       |
| **28-10-30-000** | SAF Tank Specification         | [GP-AM-AMPEL-0100-53-28-10-30-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-10/GP-AM-AMPEL-0100-53-28-10-30-000-SPEC-A.md)| SPEC     |

#### 28‑20‑00 — Distribution <a name="ata‑28‑20‑00"></a>

| Doc ID         | Title                              | File                                                                                                  | Type   |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **28-20-00-000** | Fuel Distribution Sys Desc (H2/SAF)| [GP-AM-AMPEL-0100-53-28-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-20/GP-AM-AMPEL-0100-53-28-20-00-000-SDD-A.md)  | SDD    |
| **28-20-10-000** | Pump and Valve Specification       | [GP-AM-AMPEL-0100-53-28-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-20/GP-AM-AMPEL-0100-53-28-20-10-000-SPEC-A.md)| SPEC   |
| **28-20-20-000** | Cryo-Line Insulation & Safety Spec | [GP-AM-AMPEL-0100-53-28-20-20-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-20/GP-AM-AMPEL-0100-53-28-20-20-000-SPEC-A.md)| SPEC   |

#### 28‑40‑00 — Indicating <a name="ata‑28‑40‑00"></a>

| Doc ID         | Title                         | File                                                                                                  | Type   |
| :------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **28-40-00-000** | FQIS Specification            | [GP-AM-AMPEL-0100-53-28-40-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA28_Fuel/28-40/GP-AM-AMPEL-0100-53-28-40-00-000-SPEC-A.md)| SPEC   |

---
### ATA 29 — Hydraulic Power (Actuation Focus) <a name="ata‑29"></a>

#### 29‑00‑00 — General <a name="ata‑29‑00‑00"></a>

| Doc ID         | Title                              | File                                                                                                                      | Type     |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :------- |
| **29-00-00-000** | Hydraulic Sys Ov (Actuation Focus) | [GP-AM-AMPEL-0100-53-29-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-00/GP-AM-AMPEL-0100-53-29-00-00-000-OV-A.md)     | OV, SDD  |
| **29-00-00-001** | System Specifications            | [GP-AM-AMPEL-0100-53-29-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-00/GP-AM-AMPEL-0100-53-29-00-00-001-SPEC-A.md) | SPEC     |

#### 29‑10‑00 — Electro-Hydrostatic Actuators (EHA) <a name="ata‑29‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                                      | Type     |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------------ | :------- |
| **29-10-00-000** | EHA Unit Design           | [GP-AM-AMPEL-0100-53-29-10-00-000-DD-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-10/GP-AM-AMPEL-0100-53-29-10-00-000-DD-A.md)     | DD, DWG  |
| **29-10-10-000** | EHA Performance Spec    | [GP-AM-AMPEL-0100-53-29-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-10/GP-AM-AMPEL-0100-53-29-10-10-000-SPEC-A.md)| SPEC     |

#### 29‑20‑00 — Hydraulic Lines and Fittings <a name="ata‑29‑20‑00"></a>

| Doc ID         | Title                              | File                                                                                                                      | Type   |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :----- |
| **29-20-00-000** | Hydraulic Line Routing (Redundancy)| [GP-AM-AMPEL-0100-53-29-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-20/GP-AM-AMPEL-0100-53-29-20-00-000-DWG-A.md) | DWG    |

#### 29‑30‑00 — System Monitoring <a name="ata‑29‑30‑00"></a>

| Doc ID         | Title                     | File                                                                                                                      | Type   |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------------ | :----- |
| **29-30-00-000** | Monitoring System Desc    | [GP-AM-AMPEL-0100-53-29-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-30/GP-AM-AMPEL-0100-53-29-30-00-000-SDD-A.md)  | SDD    |
| **29-30-10-000** | Sensor Specifications     | [GP-AM-AMPEL-0100-53-29-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA29_HydraulicAct/29-30/GP-AM-AMPEL-0100-53-29-30-10-000-SPEC-A.md)| SPEC   |

---
### ATA 30 — Ice and Rain Protection <a name="ata‑30"></a>

#### 30‑00‑00 — General <a name="ata‑30‑00‑00"></a>

| Doc ID         | Title                           | File                                                                                                        | Type   |
| :------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------------- | :----- |
| **30-00-00-000** | Ice and Rain Protection Overview| [GP-AM-AMPEL-0100-53-30-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-00/GP-AM-AMPEL-0100-53-30-00-00-000-OV-A.md)     | OV     |
| **30-00-00-001** | System Specifications         | [GP-AM-AMPEL-0100-53-30-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-00/GP-AM-AMPEL-0100-53-30-00-00-001-SPEC-A.md) | SPEC   |

#### 30‑10‑00 — Airfoil Protection <a name="ata‑30‑10‑00"></a>

| Doc ID         | Title                                      | File                                                                                                        | Type   |
| :------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **30-10-00-000** | Wing Anti-Ice System (Electro-Thermal)   | [GP-AM-AMPEL-0100-53-30-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-10/GP-AM-AMPEL-0100-53-30-10-00-000-SDD-A.md)    | SDD    |
| **30-10-10-000** | Wing Anti-Ice Specification              | [GP-AM-AMPEL-0100-53-30-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-10/GP-AM-AMPEL-0100-53-30-10-10-000-SPEC-A.md)| SPEC   |
| **30-10-20-000** | Wing De-Ice System (Electro-Impulse/Pneu)| [GP-AM-AMPEL-0100-53-30-10-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-10/GP-AM-AMPEL-0100-53-30-10-20-000-SDD-A.md)    | SDD    |

#### 30‑30‑00 — Nacelle Protection <a name="ata‑30‑30‑00"></a>

| Doc ID         | Title                              | File                                                                                                        | Type   |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **30-30-00-000** | Nacelle Anti-Ice System (Ref ATA 71)| [GP-AM-AMPEL-0100-53-30-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-30/GP-AM-AMPEL-0100-53-30-30-00-000-SDD-A.md)  | SDD    |
| **30-30-10-000** | Nacelle Anti-Ice Specification     | [GP-AM-AMPEL-0100-53-30-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-30/GP-AM-AMPEL-0100-53-30-30-10-000-SPEC-A.md)| SPEC   |

#### 30‑40‑00 — Window and Door Protection <a name="ata‑30‑40‑00"></a>

| Doc ID         | Title                                     | File                                                                                                        | Type   |
| :------------- | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **30-40-00-000** | Windshield Heating & Wiper (Ref ATA 56) | [GP-AM-AMPEL-0100-53-30-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-40/GP-AM-AMPEL-0100-53-30-40-00-000-SDD-A.md)    | SDD    |
| **30-40-10-000** | Windshield Heating & Wiper Spec         | [GP-AM-AMPEL-0100-53-30-40-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-40/GP-AM-AMPEL-0100-53-30-40-10-000-SPEC-A.md) | SPEC   |

#### 30‑80‑00 — Detection <a name="ata‑30‑80‑00"></a>

| Doc ID         | Title                                      | File                                                                                                        | Type   |
| :------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **30-80-00-000** | Ice Detection System Specification       | [GP-AM-AMPEL-0100-53-30-80-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-80/GP-AM-AMPEL-0100-53-30-80-00-000-SPEC-A.md)| SPEC   |
| **30-80-10-000** | AI Predictive Icing System (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-30-80-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA30_IceRain/30-80/GP-AM-AMPEL-0100-53-30-80-10-000-SDD-A.md)   | SDD    |

---
### ATA 31 — Indicating and Recording Systems <a name="ata‑31"></a>

#### 31‑00‑00 — General <a name="ata‑31‑00‑00"></a>

| Doc ID         | Title                           | File                                                                                                                | Type     |
| :------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **31-00-00-000** | Indicating & Recording Ov     | [GP-AM-AMPEL-0100-53-31-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-00/GP-AM-AMPEL-0100-53-31-00-00-000-OV-A.md)     | OV, SDD  |
| **31-00-00-001** | System Specifications           | [GP-AM-AMPEL-0100-53-31-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-00/GP-AM-AMPEL-0100-53-31-00-00-001-SPEC-A.md) | SPEC     |

#### 31‑10‑00 — Instrument and Display Systems <a name="ata‑31‑10‑00"></a>

| Doc ID         | Title                                     | File                                                                                                                | Type   |
| :------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **31-10-00-000** | Cockpit Display Spec (PFD/ND/EICAS)     | [GP-AM-AMPEL-0100-53-31-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-10/GP-AM-AMPEL-0100-53-31-10-00-000-SPEC-A.md)| SPEC   |
| **31-10-10-000** | Cockpit XAI Interface (Ref GP-COM-AI)   | [GP-AM-AMPEL-0100-53-31-10-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-10/GP-AM-AMPEL-0100-53-31-10-10-000-SDD-A.md)    | SDD    |

#### 31‑30‑00 — Recorders <a name="ata‑31‑30‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                | Type   |
| :------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **31-30-00-000** | HPC-Based Flight Data Recorder Spec   | [GP-AM-AMPEL-0100-53-31-30-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-30/GP-AM-AMPEL-0100-53-31-30-00-000-SPEC-A.md)| SPEC   |

#### 31‑60‑00 — Central Display Systems <a name="ata‑31‑60‑00"></a>

| Doc ID         | Title                                      | File                                                                                                                | Type   |
| :------------- | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **31-60-00-000** | On-Board HPC System Desc (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-31-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-60/GP-AM-AMPEL-0100-53-31-60-00-000-SDD-A.md)    | SDD    |

#### 31‑70‑00 — Data Acquisition and Fusion <a name="ata‑31‑70‑00"></a>

| Doc ID         | Title                                        | File                                                                                                                | Type   |
| :------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **31-70-00-000** | Sensor Data Acq/Fusion Arch (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-31-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-70/GP-AM-AMPEL-0100-53-31-70-00-000-SDD-A.md)    | SDD    |
| **31-70-10-000** | i-Aher0 Sensor Fusion Interface            | [GP-AM-AMPEL-0100-53-31-70-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA31_Indicating/31-70/GP-AM-AMPEL-0100-53-31-70-10-000-ICD-A.md)    | ICD    |

---
### ATA 32 — Landing Gear <a name="ata‑32"></a>

#### 32‑00‑00 — General <a name="ata‑32‑00‑00"></a>

| Doc ID         | Title                          | File                                                                                                            | Type     |
| :------------- | :----------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **32-00-00-000** | Landing Gear System Overview | [GP-AM-AMPEL-0100-53-32-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-00/GP-AM-AMPEL-0100-53-32-00-00-000-OV-A.md)   | OV, SDD  |
| **32-00-00-001** | System Specifications        | [GP-AM-AMPEL-0100-53-32-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-00/GP-AM-AMPEL-0100-53-32-00-00-001-SPEC-A.md)| SPEC     |

#### 32‑10‑00 — Main Gear <a name="ata‑32‑10‑00"></a>

| Doc ID         | Title                      | File                                                                                                            | Type   |
| :------------- | :------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-10-00-000** | Main Gear Strut & Assembly | [GP-AM-AMPEL-0100-53-32-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-10/GP-AM-AMPEL-0100-53-32-10-00-000-SDD-A.md)  | SDD    |
| **32-10-10-000** | Main Gear Assembly Drawing | [GP-AM-AMPEL-0100-53-32-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-10/GP-AM-AMPEL-0100-53-32-10-10-000-DWG-A.md)  | DWG    |

#### 32‑20‑00 — Nose Gear <a name="ata‑32‑20‑00"></a>

| Doc ID         | Title                      | File                                                                                                            | Type   |
| :------------- | :------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-20-00-000** | Nose Gear Strut & Assembly | [GP-AM-AMPEL-0100-53-32-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-20/GP-AM-AMPEL-0100-53-32-20-00-000-SDD-A.md)  | SDD    |
| **32-20-10-000** | Nose Gear Assembly Drawing | [GP-AM-AMPEL-0100-53-32-20-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-20/GP-AM-AMPEL-0100-53-32-20-10-000-DWG-A.md)  | DWG    |

#### 32‑30‑00 — Extension and Retraction <a name="ata‑32‑30‑00"></a>

| Doc ID         | Title                                  | File                                                                                                            | Type   |
| :------------- | :------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-30-00-000** | Actuation System Desc (Ref ATA 13/29)| [GP-AM-AMPEL-0100-53-32-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-30/GP-AM-AMPEL-0100-53-32-30-00-000-SDD-A.md)  | SDD    |
| **32-30-10-000** | Actuation Specification              | [GP-AM-AMPEL-0100-53-32-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-30/GP-AM-AMPEL-0100-53-32-30-10-000-SPEC-A.md)| SPEC   |

#### 32‑40‑00 — Wheels and Brakes <a name="ata‑32‑40‑00"></a>

| Doc ID         | Title                                          | File                                                                                                            | Type   |
| :------------- | :--------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-40-00-000** | Wheel and Tire Specification                 | [GP-AM-AMPEL-0100-53-32-40-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-40/GP-AM-AMPEL-0100-53-32-40-00-000-SPEC-A.md)| SPEC   |
| **32-40-10-000** | Braking Sys Desc (Electric/Regen)(Ref ATA 24)| [GP-AM-AMPEL-0100-53-32-40-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-40/GP-AM-AMPEL-0100-53-32-40-10-000-SDD-A.md)    | SDD    |
| **32-40-20-000** | Braking System Specification               | [GP-AM-AMPEL-0100-53-32-40-20-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-40/GP-AM-AMPEL-0100-53-32-40-20-000-SPEC-A.md)| SPEC   |

#### 32‑50‑00 — Steering <a name="ata‑32‑50‑00"></a>

| Doc ID         | Title                        | File                                                                                                            | Type   |
| :------------- | :--------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-50-00-000** | Nose Wheel Steering System   | [GP-AM-AMPEL-0100-53-32-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-50/GP-AM-AMPEL-0100-53-32-50-00-000-SDD-A.md)  | SDD    |
| **32-50-10-000** | Nose Wheel Steering Spec   | [GP-AM-AMPEL-0100-53-32-50-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-50/GP-AM-AMPEL-0100-53-32-50-10-000-SPEC-A.md)| SPEC   |

#### 32‑60‑00 — Position and Warning <a name="ata‑32‑60‑00"></a>

| Doc ID         | Title                            | File                                                                                                            | Type   |
| :------------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-60-00-000** | Gear Position Indicating System| [GP-AM-AMPEL-0100-53-32-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-60/GP-AM-AMPEL-0100-53-32-60-00-000-SDD-A.md)  | SDD    |

#### 32‑70‑00 — AI Health Monitoring <a name="ata‑32‑70‑00"></a>

| Doc ID         | Title                                       | File                                                                                                            | Type   |
| :------------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **32-70-00-000** | AI Landing Gear Health Mon Sys (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-32-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA32_LandingGear/32-70/GP-AM-AMPEL-0100-53-32-70-00-000-SDD-A.md)  | SDD    |

---
### ATA 33 — Lights <a name="ata‑33"></a>

#### 33‑00‑00 — General <a name="ata‑33‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                  | Type     |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **33-00-00-000** | Lighting System Overview| [GP-AM-AMPEL-0100-53-33-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-00/GP-AM-AMPEL-0100-53-33-00-00-000-OV-A.md)     | OV, SDD  |
| **33-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-33-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-00/GP-AM-AMPEL-0100-53-33-00-00-001-SPEC-A.md) | SPEC     |

#### 33‑10‑00 — Flight Compartment <a name="ata‑33‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                  | Type   |
| :------------- | :------------------------ | :---------------------------------------------------------------------------------------------------- | :----- |
| **33-10-00-000** | Cockpit Lighting Spec   | [GP-AM-AMPEL-0100-53-33-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-10/GP-AM-AMPEL-0100-53-33-10-00-000-SPEC-A.md)| SPEC   |

#### 33‑20‑00 — Passenger Compartments <a name="ata‑33‑20‑00"></a>

| Doc ID         | Title                                      | File                                                                                                  | Type     |
| :------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **33-20-00-000** | Cabin Lighting Sys (Quantum-Luminescent) | [GP-AM-AMPEL-0100-53-33-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-20/GP-AM-AMPEL-0100-53-33-20-00-000-SDD-A.md)    | SDD      |
| **33-20-10-000** | Cabin Lighting Specification             | [GP-AM-AMPEL-0100-53-33-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-20/GP-AM-AMPEL-0100-53-33-20-10-000-SPEC-A.md)| SPEC     |
| **33-20-20-000** | AI-Adaptive Cabin Lighting (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-33-20-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-20/GP-AM-AMPEL-0100-53-33-20-20-000-SDD-A.md)    | SDD      |

#### 33‑40‑00 — Exterior Lighting <a name="ata‑33‑40‑00"></a>

| Doc ID         | Title                              | File                                                                                                  | Type       |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------- | :--------- |
| **33-40-00-000** | Exterior Lighting List             | [GP-AM-AMPEL-0100-53-33-40-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-40/GP-AM-AMPEL-0100-53-33-40-00-000-LIST-A.md)| LIST, SPEC |
| **33-40-10-000** | Exterior Lighting Location Drawing | [GP-AM-AMPEL-0100-53-33-40-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-40/GP-AM-AMPEL-0100-53-33-40-10-000-DWG-A.md)  | DWG        |

#### 33‑50‑00 — Emergency Lighting <a name="ata‑33‑50‑00"></a>

| Doc ID         | Title                          | File                                                                                                  | Type   |
| :------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **33-50-00-000** | Emergency Lighting System Desc | [GP-AM-AMPEL-0100-53-33-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-50/GP-AM-AMPEL-0100-53-33-50-00-000-SDD-A.md)  | SDD    |
| **33-50-10-000** | Emergency Lighting Spec        | [GP-AM-AMPEL-0100-53-33-50-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA33_Lights/33-50/GP-AM-AMPEL-0100-53-33-50-10-000-SPEC-A.md)| SPEC   |

---
### ATA 34 — Navigation <a name="ata‑34"></a>

#### 34‑00‑00 — General <a name="ata‑34‑00‑00"></a>

| Doc ID         | Title                     | File                                                                                                            | Type     |
| :------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **34-00-00-000** | Navigation System Overview| [GP-AM-AMPEL-0100-53-34-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-00/GP-AM-AMPEL-0100-53-34-00-00-000-OV-A.md)     | OV, SDD, FIG |
| **34-00-00-001** | System Specifications     | [GP-AM-AMPEL-0100-53-34-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-00/GP-AM-AMPEL-0100-53-34-00-00-001-SPEC-A.md) | SPEC     |

#### 34‑10‑00 — Air Data <a name="ata‑34‑10‑00"></a>

| Doc ID         | Title                          | File                                                                                                            | Type   |
| :------------- | :----------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **34-10-00-000** | Air Data System Description    | [GP-AM-AMPEL-0100-53-34-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-10/GP-AM-AMPEL-0100-53-34-10-00-000-SDD-A.md)  | SDD    |
| **34-10-10-000** | Air Data Sensor Specification| [GP-AM-AMPEL-0100-53-34-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-10/GP-AM-AMPEL-0100-53-34-10-10-000-SPEC-A.md)| SPEC   |

#### 34‑20‑00 — Inertial Reference <a name="ata‑34‑20‑00"></a>

| Doc ID         | Title                                       | File                                                                                                            | Type   |
| :------------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **34-20-00-000** | Inertial Reference System (IRS/INS) Desc  | [GP-AM-AMPEL-0100-53-34-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-20/GP-AM-AMPEL-0100-53-34-20-00-000-SDD-A.md)  | SDD    |
| **34-20-10-000** | IRS Specification                         | [GP-AM-AMPEL-0100-53-34-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-20/GP-AM-AMPEL-0100-53-34-20-10-000-SPEC-A.md)| SPEC   |
| **34-20-20-000** | Quantum Sensor Integration (Ref GP-COM-QAO) | [GP-AM-AMPEL-0100-53-34-20-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-20/GP-AM-AMPEL-0100-53-34-20-20-000-SDD-A.md)    | SDD    |

#### 34‑40‑00 — Landing Aids <a name="ata‑34‑40‑00"></a>

| Doc ID         | Title                                       | File                                                                                                            | Type   |
| :------------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **34-40-00-000** | Landing Aid Receiver Spec (ILS/MLS/GLS)   | [GP-AM-AMPEL-0100-53-34-40-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-40/GP-AM-AMPEL-0100-53-34-40-00-000-SPEC-A.md)| SPEC   |

#### 34‑50‑00 — GNSS <a name="ata‑34‑50‑00"></a>

| Doc ID         | Title                    | File                                                                                                            | Type   |
| :------------- | :----------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **34-50-00-000** | GNSS Receiver Spec     | [GP-AM-AMPEL-0100-53-34-50-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-50/GP-AM-AMPEL-0100-53-34-50-00-000-SPEC-A.md)| SPEC   |

#### 34‑60‑00 — Independent Position Determining <a name="ata‑34‑60‑00"></a>

| Doc ID         | Title                                        | File                                                                                                            | Type   |
| :------------- | :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| **34-60-00-000** | Star Tracker System Description            | [GP-AM-AMPEL-0100-53-34-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-60/GP-AM-AMPEL-0100-53-34-60-00-000-SDD-A.md)    | SDD    |
| **34-60-10-000** | Star Tracker Spec (Near-Space)(Ref GP-AS)  | [GP-AM-AMPEL-0100-53-34-60-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-60/GP-AM-AMPEL-0100-53-34-60-10-000-SPEC-A.md)| SPEC   |

#### 34‑70‑00 — AI Route Optimization <a name="ata‑34‑70‑00"></a>

| Doc ID         | Title                                        | File                                                                                                            | Type     |
| :------------- | :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------- |
| **34-70-00-000** | AI Route Optimization Algo (Ref GP-COM-AI) | [GP-AM-AMPEL-0100-53-34-70-00-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-70/GP-AM-AMPEL-0100-53-34-70-00-000-ALGO-A.md) | ALGO, SDD|
| **34-70-10-000** | Performance Analysis                       | [GP-AM-AMPEL-0100-53-34-70-10-000-CAL-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-70/GP-AM-AMPEL-0100-53-34-70-10-000-CAL-A.md)    | CAL, RPT |
| **34-70-20-000** | QAO Navigation Interface (Ref GP-COM-QAO)  | [GP-AM-AMPEL-0100-53-34-70-20-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA34_Navigation/34-70/GP-AM-AMPEL-0100-53-34-70-20-000-ICD-A.md)    | ICD      |

---
### ATA 35 — Oxygen <a name="ata‑35"></a>

#### 35‑00‑00 — General <a name="ata‑35‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                    | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------ | :------- |
| **35-00-00-000** | Oxygen System Overview  | [GP-AM-AMPEL-0100-53-35-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-00/GP-AM-AMPEL-0100-53-35-00-00-000-OV-A.md)     | OV, SDD  |
| **35-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-35-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-00/GP-AM-AMPEL-0100-53-35-00-00-001-SPEC-A.md) | SPEC     |

#### 35‑10‑00 — Crew System <a name="ata‑35‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                    | Type   |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------ | :----- |
| **35-10-00-000** | Flight Crew System Desc   | [GP-AM-AMPEL-0100-53-35-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-10/GP-AM-AMPEL-0100-53-35-10-00-000-SDD-A.md)  | SDD    |
| **35-10-10-000** | Crew System Specification | [GP-AM-AMPEL-0100-53-35-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-10/GP-AM-AMPEL-0100-53-35-10-10-000-SPEC-A.md)| SPEC   |

#### 35‑20‑00 — Passenger System <a name="ata‑35‑20‑00"></a>

| Doc ID         | Title                              | File                                                                                                    | Type   |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------ | :----- |
| **35-20-00-000** | Passenger System Desc (Chem/Gas) | [GP-AM-AMPEL-0100-53-35-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-20/GP-AM-AMPEL-0100-53-35-20-00-000-SDD-A.md)  | SDD    |
| **35-20-10-000** | Passenger System Specification   | [GP-AM-AMPEL-0100-53-35-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-20/GP-AM-AMPEL-0100-53-35-20-10-000-SPEC-A.md)| SPEC   |

#### 35‑30‑00 — Portable Equipment <a name="ata‑35‑30‑00"></a>

| Doc ID         | Title                 | File                                                                                                    | Type       |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------------ | :--------- |
| **35-30-00-000** | Portable Equipment List | [GP-AM-AMPEL-0100-53-35-30-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA35_Oxygen/35-30/GP-AM-AMPEL-0100-53-35-30-00-000-LIST-A.md)| LIST, SPEC |

---
### ATA 36 — Pneumatic <a name="ata‑36"></a>

#### 36‑00‑00 — General <a name="ata‑36‑00‑00"></a>

| Doc ID         | Title                          | File                                                                                                        | Type     |
| :------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------------- | :------- |
| **36-00-00-000** | Pneumatic Sys Ov (Min Scope) | [GP-AM-AMPEL-0100-53-36-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA36_Pneumatic/36-00/GP-AM-AMPEL-0100-53-36-00-00-000-OV-A.md)     | OV, SDD  |
| **36-00-00-001** | System Specifications        | [GP-AM-AMPEL-0100-53-36-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA36_Pneumatic/36-00/GP-AM-AMPEL-0100-53-36-00-00-001-SPEC-A.md) | SPEC     |

#### 36‑10‑00 — Bleed Air <a name="ata‑36‑10‑00"></a>

| Doc ID         | Title                              | File                                                                                                        | Type   |
| :------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **36-10-00-000** | Bleed Air Desc (If Used)(Ref ATA 75)| [GP-AM-AMPEL-0100-53-36-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA36_Pneumatic/36-10/GP-AM-AMPEL-0100-53-36-10-00-000-SDD-A.md)  | SDD    |
| **36-10-10-000** | Bleed Air Ducting Dwg (If Used)  | [GP-AM-AMPEL-0100-53-36-10-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA36_Pneumatic/36-10/GP-AM-AMPEL-0100-53-36-10-10-000-DWG-A.md)  | DWG    |

#### 36‑20‑00 — Indication <a name="ata‑36‑20‑00"></a>

| Doc ID         | Title                                | File                                                                                                        | Type   |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **36-20-00-000** | Pneumatic Sys Indication (If Appl) | [GP-AM-AMPEL-0100-53-36-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA36_Pneumatic/36-20/GP-AM-AMPEL-0100-53-36-20-00-000-SDD-A.md)  | SDD    |

---
### ATA 37 — Vacuum <a name="ata‑37"></a>

#### 37‑00‑00 — General <a name="ata‑37‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                  | Type     |
| :------------- | :-------------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **37-00-00-000** | Vacuum System Ov (If Appl)| [GP-AM-AMPEL-0100-53-37-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA37_Vacuum/37-00/GP-AM-AMPEL-0100-53-37-00-00-000-OV-A.md)     | OV, SDD  |
| **37-00-00-001** | System Specifications     | [GP-AM-AMPEL-0100-53-37-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA37_Vacuum/37-00/GP-AM-AMPEL-0100-53-37-00-00-001-SPEC-A.md) | SPEC     |

#### 37‑10‑00 — Lines and Components <a name="ata‑37‑10‑00"></a>

| Doc ID         | Title                    | File                                                                                                  | Type   |
| :------------- | :----------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **37-10-00-000** | Vacuum Line Drawing    | [GP-AM-AMPEL-0100-53-37-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA37_Vacuum/37-10/GP-AM-AMPEL-0100-53-37-10-00-000-DWG-A.md)  | DWG    |
| **37-10-10-000** | Component Specifications | [GP-AM-AMPEL-0100-53-37-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA37_Vacuum/37-10/GP-AM-AMPEL-0100-53-37-10-10-000-SPEC-A.md)| SPEC   |

#### 37‑20‑00 — Indication <a name="ata‑37‑20‑00"></a>

| Doc ID         | Title                     | File                                                                                                  | Type   |
| :------------- | :------------------------ | :---------------------------------------------------------------------------------------------------- | :----- |
| **37-20-00-000** | Vacuum System Indication Desc | [GP-AM-AMPEL-0100-53-37-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA37_Vacuum/37-20/GP-AM-AMPEL-0100-53-37-20-00-000-SDD-A.md)  | SDD    |

---
### ATA 38 — Water and Waste <a name="ata‑38"></a>

#### 38‑00‑00 — General <a name="ata‑38‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                          | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------------ | :------- |
| **38-00-00-000** | Water and Waste Overview| [GP-AM-AMPEL-0100-53-38-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-00/GP-AM-AMPEL-0100-53-38-00-00-000-OV-A.md)   | OV, SDD  |
| **38-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-38-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-00/GP-AM-AMPEL-0100-53-38-00-00-001-SPEC-A.md)| SPEC     |

#### 38‑10‑00 — Potable Water <a name="ata‑38‑10‑00"></a>

| Doc ID         | Title                                      | File                                                                                                          | Type   |
| :------------- | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **38-10-00-000** | Potable Water System Description         | [GP-AM-AMPEL-0100-53-38-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-10/GP-AM-AMPEL-0100-53-38-10-00-000-SDD-A.md)  | SDD    |
| **38-10-10-000** | Potable Water Specification              | [GP-AM-AMPEL-0100-53-38-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-10/GP-AM-AMPEL-0100-53-38-10-10-000-SPEC-A.md)| SPEC   |
| **38-10-20-000** | Advanced Filtration/Recycling (Ref ATA 21)| [GP-AM-AMPEL-0100-53-38-10-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-10/GP-AM-AMPEL-0100-53-38-10-20-000-SDD-A.md)    | SDD    |

#### 38‑30‑00 — Lavatory Waste <a name="ata‑38‑30‑00"></a>

| Doc ID         | Title                       | File                                                                                                          | Type   |
| :------------- | :-------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **38-30-00-000** | Lavatory Waste System Desc  | [GP-AM-AMPEL-0100-53-38-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-30/GP-AM-AMPEL-0100-53-38-30-00-000-SDD-A.md)  | SDD    |
| **38-30-10-000** | Lavatory Waste Specification| [GP-AM-AMPEL-0100-53-38-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-30/GP-AM-AMPEL-0100-53-38-30-10-000-SPEC-A.md)| SPEC   |
| **38-30-20-000** | Eco-Lavatory Technology     | [GP-AM-AMPEL-0100-53-38-30-20-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA38_WaterWaste/38-30/GP-AM-AMPEL-0100-53-38-30-20-000-SDD-A.md)    | SDD    |

---
### ATA 39 — Electrical/Electronic Panels <a name="ata‑39"></a>

#### 39‑00‑00 — General <a name="ata‑39‑00‑00"></a>

| Doc ID         | Title                           | File                                                                                                      | Type     |
| :------------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------- | :------- |
| **39-00-00-000** | Electrical/Electronic Panels Ov | [GP-AM-AMPEL-0100-53-39-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA39_Panels/39-00/GP-AM-AMPEL-0100-53-39-00-00-000-OV-A.md)     | OV, SDD  |
| **39-00-00-001** | Specifications and Standards  | [GP-AM-AMPEL-0100-53-39-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA39_Panels/39-00/GP-AM-AMPEL-0100-53-39-00-00-001-SPEC-A.md) | SPEC     |

#### 39‑10‑00 — Instrument Panels <a name="ata‑39‑10‑00"></a>

| Doc ID         | Title                                     | File                                                                                                      | Type   |
| :------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **39-10-00-000** | Instrument Panel Layout (Ref ATA 31)    | [GP-AM-AMPEL-0100-53-39-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA39_Panels/39-10/GP-AM-AMPEL-0100-53-39-10-00-000-DWG-A.md)  | DWG    |
| **39-10-10-000** | Instrument Panel Component Spec       | [GP-AM-AMPEL-0100-53-39-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA39_Panels/39-10/GP-AM-AMPEL-0100-53-39-10-10-000-SPEC-A.md)| SPEC   |

#### 39‑20‑00 — Control Panels <a name="ata‑39‑20‑00"></a>

| Doc ID         | Title                                     | File                                                                                                      | Type   |
| :------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **39-20-00-000** | Control Panel Layout (Ref ATA 27, 76)   | [GP-AM-AMPEL-0100-53-39-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA39_Panels/39-20/GP-AM-AMPEL-0100-53-39-20-00-000-DWG-A.md)  | DWG    |
| **39-20-10-000** | Control Panel Component Spec          | [GP-AM-AMPEL-0100-53-39-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA39_Panels/39-20/GP-AM-AMPEL-0100-53-39-20-10-000-SPEC-A.md)| SPEC   |

---
### ATA 41 — Water Ballast <a name="ata‑41"></a>

#### 41‑00‑00 — General <a name="ata‑41‑00‑00"></a>

| Doc ID         | Title                             | File                                                                                                                | Type     |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **41-00-00-000** | Water Ballast Sys Ov (If Appl)  | [GP-AM-AMPEL-0100-53-41-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA41_WaterBallast/41-00/GP-AM-AMPEL-0100-53-41-00-00-000-OV-A.md)   | OV, SDD  |
| **41-00-00-001** | System Specifications           | [GP-AM-AMPEL-0100-53-41-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA41_WaterBallast/41-00/GP-AM-AMPEL-0100-53-41-00-00-001-SPEC-A.md)| SPEC     |

#### 41‑10‑00 — Tanks <a name="ata‑41‑10‑00"></a>

| Doc ID         | Title                   | File                                                                                                                | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **41-10-00-000** | Tank Design & Location  | [GP-AM-AMPEL-0100-53-41-10-00-000-DD-A.md](./GP-AM/AMPEL_0100/ATA41_WaterBallast/41-10/GP-AM-AMPEL-0100-53-41-10-00-000-DD-A.md)     | DD, DWG  |
| **41-10-10-000** | Tank Specification      | [GP-AM-AMPEL-0100-53-41-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA41_WaterBallast/41-10/GP-AM-AMPEL-0100-53-41-10-10-000-SPEC-A.md)| SPEC     |

#### 41‑20‑00 — Distribution <a name="ata‑41‑20‑00"></a>

| Doc ID         | Title                        | File                                                                                                                | Type   |
| :------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **41-20-00-000** | Distribution System Desc   | [GP-AM-AMPEL-0100-53-41-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA41_WaterBallast/41-20/GP-AM-AMPEL-0100-53-41-20-00-000-SDD-A.md)  | SDD    |
| **41-20-10-000** | Pump and Valve Specification | [GP-AM-AMPEL-0100-53-41-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA41_WaterBallast/41-20/GP-AM-AMPEL-0100-53-41-20-10-000-SPEC-A.md)| SPEC   |

---
### ATA 42 — Integrated Modular Avionics (IMA) <a name="ata‑42"></a>

#### 42‑00‑00 — General <a name="ata‑42‑00‑00"></a>

| Doc ID         | Title                             | File                                                                                                | Type     |
| :------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------- | :------- |
| **42-00-00-000** | IMA System Overview             | [GP-AM-AMPEL-0100-53-42-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-00/GP-AM-AMPEL-0100-53-42-00-00-000-OV-A.md)       | OV, SDD  |
| **42-00-00-001** | IMA Architecture Spec (ARINC 653)| [GP-AM-AMPEL-0100-53-42-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-00/GP-AM-AMPEL-0100-53-42-00-00-001-SPEC-A.md) | SPEC     |

#### 42‑10‑00 — Core Processing Modules (CPM) <a name="ata‑42‑10‑00"></a>

| Doc ID         | Title                                       | File                                                                                                | Type     |
| :------------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------- | :------- |
| **42-10-00-000** | Core Processing Module Spec             | [GP-AM-AMPEL-0100-53-42-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-10/GP-AM-AMPEL-0100-53-42-10-00-000-SPEC-A.md)| SPEC     |
| **42-10-10-000** | Quantum Co-processor Int (Ref GP-COM-QAO) | [GP-AM-AMPEL-0100-53-42-10-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-10/GP-AM-AMPEL-0100-53-42-10-10-000-SDD-A.md)    | SDD, ICD |

#### 42‑20‑00 — Network <a name="ata‑42‑20‑00"></a>

| Doc ID         | Title                              | File                                                                                                | Type     |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------- | :------- |
| **42-20-00-000** | Avionics Network Spec (e.g., AFDX) | [GP-AM-AMPEL-0100-53-42-20-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-20/GP-AM-AMPEL-0100-53-42-20-00-000-SPEC-A.md)| SPEC     |
| **42-20-10-000** | Network Topology Diagram         | [GP-AM-AMPEL-0100-53-42-20-10-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-20/GP-AM-AMPEL-0100-53-42-20-10-000-DWG-A.md)  | DWG, FIG |

#### 42‑30‑00 — Time Distribution <a name="ata‑42‑30‑00"></a>

| Doc ID         | Title                                | File                                                                                                | Type   |
| :------------- | :----------------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **42-30-00-000** | Time Distribution Protocol Spec    | [GP-AM-AMPEL-0100-53-42-30-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA42_IMA/42-30/GP-AM-AMPEL-0100-53-42-30-00-000-SPEC-A.md)| SPEC   |

---
### ATA 44 — Cabin Systems <a name="ata‑44"></a>

#### 44‑00‑00 — General <a name="ata‑44‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                                | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **44-00-00-000** | Cabin Systems Overview  | [GP-AM-AMPEL-0100-53-44-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-00/GP-AM-AMPEL-0100-53-44-00-00-000-OV-A.md)     | OV, SDD  |
| **44-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-44-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-00/GP-AM-AMPEL-0100-53-44-00-00-001-SPEC-A.md) | SPEC     |

#### 44‑10‑00 — In-Flight Entertainment (IFE) <a name="ata‑44‑10‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                | Type   |
| :------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **44-10-00-000** | IFE Sys Desc (VR/AR Int)(Ref ATA 25)  | [GP-AM-AMPEL-0100-53-44-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-10/GP-AM-AMPEL-0100-53-44-10-00-000-SDD-A.md)  | SDD    |
| **44-10-10-000** | IFE Component Specification           | [GP-AM-AMPEL-0100-53-44-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-10/GP-AM-AMPEL-0100-53-44-10-10-000-SPEC-A.md)| SPEC   |
| **44-10-20-000** | IFE Network Interface (Ref ATA 46)    | [GP-AM-AMPEL-0100-53-44-10-20-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-10/GP-AM-AMPEL-0100-53-44-10-20-000-ICD-A.md)    | ICD    |

#### 44‑20‑00 — Cabin Management System (CMS) <a name="ata‑44‑20‑00"></a>

| Doc ID         | Title                                        | File                                                                                                                | Type   |
| :------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **44-20-00-000** | CMS Desc (Lighting/Temp)(Ref ATA 21, 33)   | [GP-AM-AMPEL-0100-53-44-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-20/GP-AM-AMPEL-0100-53-44-20-00-000-SDD-A.md)    | SDD    |
| **44-20-10-000** | CMS Component Specification                | [GP-AM-AMPEL-0100-53-44-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-20/GP-AM-AMPEL-0100-53-44-20-10-000-SPEC-A.md) | SPEC   |
| **44-20-20-000** | AI Personalization Interface (Ref GP-COM-AI) | [GP-AM-AMPEL-0100-53-44-20-20-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA44_CabinSystems/44-20/GP-AM-AMPEL-0100-53-44-20-20-000-ICD-A.md)    | ICD    |

---
### ATA 45 — Central Maintenance System (CMS) <a name="ata‑45"></a>

#### 45‑00‑00 — General <a name="ata‑45‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                | Type     |
| :------------- | :---------------------- | :-------------------------------------------------------------------------------------------------- | :------- |
| **45-00-00-000** | CMS Overview            | [GP-AM-AMPEL-0100-53-45-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-00/GP-AM-AMPEL-0100-53-45-00-00-000-OV-A.md)       | OV, SDD  |
| **45-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-45-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-00/GP-AM-AMPEL-0100-53-45-00-00-001-SPEC-A.md) | SPEC     |

#### 45‑10‑00 — Central Maintenance Computer (CMC) <a name="ata‑45‑10‑00"></a>

| Doc ID         | Title                      | File                                                                                                | Type   |
| :------------- | :------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **45-10-00-000** | CMC Hardware Specification | [GP-AM-AMPEL-0100-53-45-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-10/GP-AM-AMPEL-0100-53-45-10-00-000-SPEC-A.md)| SPEC   |

#### 45‑20‑00 — Software <a name="ata‑45‑20‑00"></a>

| Doc ID         | Title                    | File                                                                                                | Type   |
| :------------- | :----------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **45-20-00-000** | CMS Software Architecture| [GP-AM-AMPEL-0100-53-45-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-20/GP-AM-AMPEL-0100-53-45-20-00-000-SDD-A.md)    | SDD    |

#### 45‑40‑00 — Health Reporting <a name="ata‑45‑40‑00"></a>

| Doc ID         | Title                             | File                                                                                                | Type   |
| :------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **45-40-00-000** | Health Reporting Formats        | [GP-AM-AMPEL-0100-53-45-40-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-40/GP-AM-AMPEL-0100-53-45-40-00-000-SPEC-A.md)| SPEC   |
| **45-40-10-000** | Ground System Interface (Ref GP-GRO)| [GP-AM-AMPEL-0100-53-45-40-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-40/GP-AM-AMPEL-0100-53-45-40-10-000-ICD-A.md)    | ICD    |

#### 45‑50‑00 — AI Diagnostics <a name="ata‑45‑50‑00"></a>

| Doc ID         | Title                                       | File                                                                                                | Type   |
| :------------- | :------------------------------------------ | :-------------------------------------------------------------------------------------------------- | :----- |
| **45-50-00-000** | AI Diagnostic Engine Desc (Ref GP-COM-AI) | [GP-AM-AMPEL-0100-53-45-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-50/GP-AM-AMPEL-0100-53-45-50-00-000-SDD-A.md)    | SDD    |
| **45-50-10-000** | Predictive Maint Algos (Ref ATA 05)       | [GP-AM-AMPEL-0100-53-45-50-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-50/GP-AM-AMPEL-0100-53-45-50-10-000-ALGO-A.md) | ALGO   |

#### 45‑60‑00 — Digital Twin Orchestration (DTO) <a name="ata‑45‑60‑00"></a>

| Doc ID         | Title                                | File                                                                                                | Type   |
| :------------- | :----------------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **45-60-00-000** | CMS to DTO Interface (Ref GP-COM-DTO)| [GP-AM-AMPEL-0100-53-45-60-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-60/GP-AM-AMPEL-0100-53-45-60-00-000-ICD-A.md)    | ICD    |
| **45-60-10-000** | Maintenance Data Synchronization   | [GP-AM-AMPEL-0100-53-45-60-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA45_CMS/45-60/GP-AM-AMPEL-0100-53-45-60-10-000-SDD-A.md)    | SDD    |

---
### ATA 46 — Information Systems <a name="ata‑46"></a>

#### 46‑00‑00 — General <a name="ata‑46‑00‑00"></a>

| Doc ID         | Title                              | File                                                                                                                  | Type     |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :------- |
| **46-00-00-000** | Information Systems Overview     | [GP-AM-AMPEL-0100-53-46-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-00/GP-AM-AMPEL-0100-53-46-00-00-000-OV-A.md)     | OV, SDD  |
| **46-00-00-001** | Sys Specs & Security Standards   | [GP-AM-AMPEL-0100-53-46-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-00/GP-AM-AMPEL-0100-53-46-00-00-001-SPEC-A.md) | SPEC     |

#### 46‑10‑00 — GQP Interface <a name="ata‑46‑10‑00"></a>

| Doc ID         | Title                                      | File                                                                                                                  | Type   |
| :------------- | :----------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----- |
| **46-10-00-000** | GAIA Quantum Platform (GQP) Int (Ref GP-COM-QAO)| [GP-AM-AMPEL-0100-53-46-10-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-10/GP-AM-AMPEL-0100-53-46-10-00-000-ICD-A.md)    | ICD    |

#### 46‑20‑00 — Electronic Flight Bag (EFB) <a name="ata‑46‑20‑00"></a>

| Doc ID         | Title                            | File                                                                                                                  | Type   |
| :------------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----- |
| **46-20-00-000** | EFB Hardware & Software Spec   | [GP-AM-AMPEL-0100-53-46-20-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-20/GP-AM-AMPEL-0100-53-46-20-00-000-SPEC-A.md)| SPEC   |

#### 46‑30‑00 — IFE Network <a name="ata‑46‑30‑00"></a>

| Doc ID         | Title                                    | File                                                                                                                  | Type   |
| :------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----- |
| **46-30-00-000** | IFE Network Architecture Desc (Ref ATA 44)| [GP-AM-AMPEL-0100-53-46-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-30/GP-AM-AMPEL-0100-53-46-30-00-000-SDD-A.md)    | SDD    |

#### 46‑60‑00 — BITT Ledger Integration <a name="ata‑46‑60‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                  | Type   |
| :------------- | :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----- |
| **46-60-00-000** | BITT Data Interface Spec (Ref GP-COM-BITT)| [GP-AM-AMPEL-0100-53-46-60-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-60/GP-AM-AMPEL-0100-53-46-60-00-000-ICD-A.md)    | ICD    |

#### 46‑63‑00 — QAO On-Board Interface <a name="ata‑46‑63‑00"></a>

| Doc ID         | Title                                           | File                                                                                                                  | Type     |
| :------------- | :---------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :------- |
| **46-63-00-000** | Quantum Algorithm Orch (QAO) Int (Ref GP-COM-QAO)| [GP-AM-AMPEL-0100-53-46-63-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-63/GP-AM-AMPEL-0100-53-46-63-00-000-SDD-A.md)    | SDD, ICD |

#### 46‑70‑00 — Cybersecurity Functions <a name="ata‑46‑70‑00"></a>

| Doc ID         | Title                                        | File                                                                                                                  | Type     |
| :------------- | :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :------- |
| **46-70-00-000** | Cybersecurity Req & Impl (Ref ATA 23-80)   | [GP-AM-AMPEL-0100-53-46-70-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-70/GP-AM-AMPEL-0100-53-46-70-00-000-SPEC-A.md) | SPEC, SDD|
| **46-70-10-000** | Intrusion Detection System (AI)(Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-46-70-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA46_InfoSystems/46-70/GP-AM-AMPEL-0100-53-46-70-10-000-SDD-A.md)    | SDD      |

---
### ATA 47 — Nitrogen Generation System (NGS) <a name="ata‑47"></a>

#### 47‑00‑00 — General <a name="ata‑47‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                              | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------ | :------- |
| **47-00-00-000** | NGS Overview            | [GP-AM-AMPEL-0100-53-47-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-00/GP-AM-AMPEL-0100-53-47-00-00-000-OV-A.md)       | OV, SDD  |
| **47-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-47-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-00/GP-AM-AMPEL-0100-53-47-00-00-001-SPEC-A.md) | SPEC     |

#### 47‑10‑00 — Air Separation Module (ASM) <a name="ata‑47‑10‑00"></a>

| Doc ID         | Title                   | File                                                                                              | Type   |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **47-10-00-000** | ASM Specification       | [GP-AM-AMPEL-0100-53-47-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-10/GP-AM-AMPEL-0100-53-47-10-00-000-SPEC-A.md)| SPEC   |
| **47-10-10-000** | ASM Maintenance Manual  | [GP-AM-AMPEL-0100-53-47-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-10/GP-AM-AMPEL-0100-53-47-10-10-000-MAN-A.md)  | MAN    |

#### 47‑20‑00 — Distribution <a name="ata‑47‑20‑00"></a>

| Doc ID         | Title                                | File                                                                                              | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **47-20-00-000** | NEA Distribution Diagram (Ref ATA 28)| [GP-AM-AMPEL-0100-53-47-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-20/GP-AM-AMPEL-0100-53-47-20-00-000-DWG-A.md)  | DWG    |

#### 47‑30‑00 — Control and Monitoring <a name="ata‑47‑30‑00"></a>

| Doc ID         | Title                             | File                                                                                              | Type   |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **47-30-00-000** | Control System Description      | [GP-AM-AMPEL-0100-53-47-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-30/GP-AM-AMPEL-0100-53-47-30-00-000-SDD-A.md)  | SDD    |
| **47-30-10-000** | Sensor Spec (Oxygen Concentration)| [GP-AM-AMPEL-0100-53-47-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA47_NGS/47-30/GP-AM-AMPEL-0100-53-47-30-10-000-SPEC-A.md)| SPEC   |

---
### ATA 48 — Reserved for Future Use <a name="ata‑48"></a>

#### 48‑00‑00 — General <a name="ata‑48‑00‑00"></a>

| Doc ID         | Title           | File                                                                                                        | Type   |
| :------------- | :-------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **48-00-00-000** | Chapter Reserved| [GP-AM-AMPEL-0100-53-48-00-00-000-NOTE-A.md](./GP-AM/AMPEL_0100/ATA48_Reserved/48-00/GP-AM-AMPEL-0100-53-48-00-00-000-NOTE-A.md)| NOTE   |

---
### ATA 49 — Airborne Auxiliary Power (AAP/APU) <a name="ata‑49"></a>

#### 49‑00‑00 — General <a name="ata‑49‑00‑00"></a>

| Doc ID         | Title                                | File                                                                                              | Type     |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------ | :------- |
| **49-00-00-000** | APU System Ov (Turbine/FC/Hybrid)| [GP-AM-AMPEL-0100-53-49-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA49_APU/49-00/GP-AM-AMPEL-0100-53-49-00-00-000-OV-A.md)     | OV, SDD  |
| **49-00-00-001** | System Specifications              | [GP-AM-AMPEL-0100-53-49-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA49_APU/49-00/GP-AM-AMPEL-0100-53-49-00-00-001-SPEC-A.md) | SPEC     |

#### 49‑10‑00 — Power Plant <a name="ata‑49‑10‑00"></a>

| Doc ID         | Title                                | File                                                                                              | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **49-10-00-000** | APU Core Description (Ref ATA 85 if FC)| [GP-AM-AMPEL-0100-53-49-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA49_APU/49-10/GP-AM-AMPEL-0100-53-49-10-00-000-SDD-A.md)    | SDD    |
| **49-10-10-000** | APU Maintenance Manual               | [GP-AM-AMPEL-0100-53-49-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA49_APU/49-10/GP-AM-AMPEL-0100-53-49-10-10-000-MAN-A.md)  | MAN    |

#### 49‑70‑00 — Starting <a name="ata‑49‑70‑00"></a>

| Doc ID         | Title                              | File                                                                                              | Type   |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **49-70-00-000** | Starting System Desc (Ref ATA 80)| [GP-AM-AMPEL-0100-53-49-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA49_APU/49-70/GP-AM-AMPEL-0100-53-49-70-00-000-SDD-A.md)    | SDD    |

---
### ATA 50 — Cargo and Accessory Compartments <a name="ata‑50"></a>

#### 50‑00‑00 — General <a name="ata‑50‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                | Type     |
| :------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------- | :------- |
| **50-00-00-000** | Compartments Overview     | [GP-AM-AMPEL-0100-53-50-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA50_Cargo/50-00/GP-AM-AMPEL-0100-53-50-00-00-000-OV-A.md)     | OV, SDD  |
| **50-00-00-001** | Compartment Layout Drawings | [GP-AM-AMPEL-0100-53-50-00-00-001-DWG-A.md](./GP-AM/AMPEL_0100/ATA50_Cargo/50-00/GP-AM-AMPEL-0100-53-50-00-00-001-DWG-A.md)  | DWG      |

#### 50‑10‑00 — Cargo Compartment <a name="ata‑50‑10‑00"></a>

| Doc ID         | Title                                     | File                                                                                                | Type   |
| :------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **50-10-00-000** | Cargo Loading Sys Desc (Manual/Automated) | [GP-AM-AMPEL-0100-53-50-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA50_Cargo/50-10/GP-AM-AMPEL-0100-53-50-10-00-000-SDD-A.md)    | SDD    |
| **50-10-10-000** | ULD Specifications                      | [GP-AM-AMPEL-0100-53-50-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA50_Cargo/50-10/GP-AM-AMPEL-0100-53-50-10-10-000-SPEC-A.md)| SPEC   |
| **50-10-20-000** | Automated Loading Robot Int (Ref GP-RAME)| [GP-AM-AMPEL-0100-53-50-10-20-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA50_Cargo/50-10/GP-AM-AMPEL-0100-53-50-10-20-000-ICD-A.md)    | ICD    |

#### 50‑20‑00 — Accessory Compartments <a name="ata‑50‑20‑00"></a>

| Doc ID         | Title                            | File                                                                                                | Type     |
| :------------- | :------------------------------- | :-------------------------------------------------------------------------------------------------- | :------- |
| **50-20-00-000** | Accessory Compartment List & Access| [GP-AM-AMPEL-0100-53-50-20-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA50_Cargo/50-20/GP-AM-AMPEL-0100-53-50-20-00-000-LIST-A.md)| LIST, DWG|

---
### ATA 51 — Structures – General <a name="ata‑51"></a>

#### 51‑00‑00 — General <a name="ata‑51‑00‑00"></a>

| Doc ID         | Title                          | File                                                                                                              | Type     |
| :------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **51-00-00-000** | Structural Philosophy Overview | [GP-AM-AMPEL-0100-53-51-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-00/GP-AM-AMPEL-0100-53-51-00-00-000-OV-A.md)     | OV, SDD  |
| **51-00-00-001** | Structural Design Criteria     | [GP-AM-AMPEL-0100-53-51-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-00/GP-AM-AMPEL-0100-53-51-00-00-001-SPEC-A.md) | SPEC, REQ|

#### 51‑10‑00 — Materials and Processes <a name="ata‑51‑10‑00"></a>

| Doc ID         | Title                                           | File                                                                                                              | Type     |
| :------------- | :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **51-10-00-000** | Primary Structural Materials List             | [GP-AM-AMPEL-0100-53-51-10-00-000-LIST-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-10/GP-AM-AMPEL-0100-53-51-10-00-000-LIST-A.md)| LIST, SPEC |
| **51-10-10-000** | Advanced Composite Spec (BNNT/Lattice)(Ref ATA 20)| [GP-AM-AMPEL-0100-53-51-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-10/GP-AM-AMPEL-0100-53-51-10-10-000-SPEC-A.md)| SPEC     |
| **51-10-20-000** | Standard Repair Procedures                    | [GP-AM-AMPEL-0100-53-51-10-20-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-10/GP-AM-AMPEL-0100-53-51-10-20-000-PROC-A.md)| PROC     |

#### 51‑20‑00 — Analysis Methods <a name="ata‑51‑20‑00"></a>

| Doc ID         | Title                                       | File                                                                                                              | Type     |
| :------------- | :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **51-20-00-000** | Structural Analysis Methodology             | [GP-AM-AMPEL-0100-53-51-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-20/GP-AM-AMPEL-0100-53-51-20-00-000-SDD-A.md)    | SDD, ANA |
| **51-20-10-000** | Fatigue and Damage Tolerance Analysis Rpt | [GP-AM-AMPEL-0100-53-51-20-10-000-RPT-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-20/GP-AM-AMPEL-0100-53-51-20-10-000-RPT-A.md)    | RPT, ANA |

#### 51‑70‑00 — Structural Health Monitoring (SHM) <a name="ata‑51‑70‑00"></a>

| Doc ID         | Title                                            | File                                                                                                              | Type     |
| :------------- | :----------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **51-70-00-000** | SHM System Architecture Desc                   | [GP-AM-AMPEL-0100-53-51-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-70/GP-AM-AMPEL-0100-53-51-70-00-000-SDD-A.md)    | SDD      |
| **51-70-10-000** | Sensor Spec (Fiber Optic/Piezo)                | [GP-AM-AMPEL-0100-53-51-70-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-70/GP-AM-AMPEL-0100-53-51-70-10-000-SPEC-A.md) | SPEC     |
| **51-70-20-000** | AI Damage Detection Algos (Ref GP-COM-AI)      | [GP-AM-AMPEL-0100-53-51-70-20-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-70/GP-AM-AMPEL-0100-53-51-70-20-000-ALGO-A.md) | ALGO, SDD|
| **51-70-30-000** | SHM Data Int to DTO/CMS (Ref ATA 45, GP-COM-DTO)| [GP-AM-AMPEL-0100-53-51-70-30-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA51_Structures/51-70/GP-AM-AMPEL-0100-53-51-70-30-000-ICD-A.md)    | ICD      |

---
### ATA 52 — Doors <a name="ata‑52"></a>

#### 52‑00‑00 — General <a name="ata‑52‑00‑00"></a>

| Doc ID         | Title                     | File                                                                                              | Type     |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------ | :------- |
| **52-00-00-000** | Doors Overview            | [GP-AM-AMPEL-0100-53-52-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-00/GP-AM-AMPEL-0100-53-52-00-00-000-OV-A.md)       | OV, SDD  |
| **52-00-00-001** | Door Design Specs       | [GP-AM-AMPEL-0100-53-52-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-00/GP-AM-AMPEL-0100-53-52-00-00-001-SPEC-A.md) | SPEC     |

#### 52‑10‑00 — Passenger Doors <a name="ata‑52‑10‑00"></a>

| Doc ID         | Title                         | File                                                                                              | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **52-10-00-000** | Passenger Door Mechanism Desc | [GP-AM-AMPEL-0100-53-52-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-10/GP-AM-AMPEL-0100-53-52-10-00-000-SDD-A.md)  | SDD    |
| **52-10-10-000** | Passenger Door Maint Manual   | [GP-AM-AMPEL-0100-53-52-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-10/GP-AM-AMPEL-0100-53-52-10-10-000-MAN-A.md)  | MAN    |

#### 52‑30‑00 — Cargo Doors <a name="ata‑52‑30‑00"></a>

| Doc ID         | Title                                | File                                                                                              | Type   |
| :------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **52-30-00-000** | Cargo Door Mechanism Desc (Ref ATA 50)| [GP-AM-AMPEL-0100-53-52-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-30/GP-AM-AMPEL-0100-53-52-30-00-000-SDD-A.md)  | SDD    |
| **52-30-10-000** | Cargo Door Maintenance Manual      | [GP-AM-AMPEL-0100-53-52-30-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-30/GP-AM-AMPEL-0100-53-52-30-10-000-MAN-A.md)  | MAN    |

#### 52‑70‑00 — Smart Door Systems <a name="ata‑52‑70‑00"></a>

| Doc ID         | Title                                           | File                                                                                              | Type     |
| :------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------ | :------- |
| **52-70-00-000** | Integrated Sensor & Health Mon (Ref ATA 31, 51-70)| [GP-AM-AMPEL-0100-53-52-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA52_Doors/52-70/GP-AM-AMPEL-0100-53-52-70-00-000-SDD-A.md)    | SDD, SPEC|

---
### ATA 53 — Fuselage <a name="ata‑53"></a>

#### 53‑00‑00 — General <a name="ata‑53‑00‑00"></a>

| Doc ID         | Title                              | File                                                                                                          | Type     |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------ | :------- |
| **53-00-00-000** | Fuselage Structure Overview      | [GP-AM-AMPEL-0100-53-53-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-00/GP-AM-AMPEL-0100-53-53-00-00-000-OV-A.md)     | OV, SDD  |
| **53-00-00-001** | Fuselage Design Specifications   | [GP-AM-AMPEL-0100-53-53-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-00/GP-AM-AMPEL-0100-53-53-00-00-001-SPEC-A.md)| SPEC     |
| **53-00-00-002** | Fuselage Gen Arrangement Drawing | [GP-AM-AMPEL-0100-53-53-00-00-002-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-00/GP-AM-AMPEL-0100-53-53-00-00-002-DWG-A.md)  | DWG      |

#### 53‑10‑00 — Nose Station <a name="ata‑53‑10‑00"></a>

| Doc ID         | Title                         | File                                                                                                          | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-10-00-000** | Nose Section Structural Drawing | [GP-AM-AMPEL-0100-53-53-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-10/GP-AM-AMPEL-0100-53-53-10-00-000-DWG-A.md)  | DWG    |
| **53-10-10-000** | Nose Section Repair Manual    | [GP-AM-AMPEL-0100-53-53-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-10/GP-AM-AMPEL-0100-53-53-10-10-000-MAN-A.md)  | MAN    |

#### 53‑20‑00 — Forward Station <a name="ata‑53‑20‑00"></a>

| Doc ID         | Title                           | File                                                                                                          | Type   |
| :------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-20-00-000** | Forward Section Structural Dwg| [GP-AM-AMPEL-0100-53-53-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-20/GP-AM-AMPEL-0100-53-53-20-00-000-DWG-A.md)  | DWG    |
| **53-20-10-000** | Forward Section Repair Manual   | [GP-AM-AMPEL-0100-53-53-20-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-20/GP-AM-AMPEL-0100-53-53-20-10-000-MAN-A.md)  | MAN    |

#### 53‑30‑00 — Center Station <a name="ata‑53‑30‑00"></a>

| Doc ID         | Title                                         | File                                                                                                          | Type   |
| :------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-30-00-000** | Center Section Structural Dwg (Wing Int)(Ref ATA 57)| [GP-AM-AMPEL-0100-53-53-30-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-30/GP-AM-AMPEL-0100-53-53-30-00-000-DWG-A.md)  | DWG    |
| **53-30-10-000** | Center Section Repair Manual                | [GP-AM-AMPEL-0100-53-53-30-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-30/GP-AM-AMPEL-0100-53-53-30-10-000-MAN-A.md)  | MAN    |

#### 53‑40‑00 — Belly Station <a name="ata‑53‑40‑00"></a>

| Doc ID         | Title                                        | File                                                                                                          | Type   |
| :------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-40-00-000** | Belly Section Structural Dwg (LG Int)(Ref ATA 32)| [GP-AM-AMPEL-0100-53-53-40-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-40/GP-AM-AMPEL-0100-53-53-40-00-000-DWG-A.md)  | DWG    |
| **53-40-10-000** | Belly Section Repair Manual                | [GP-AM-AMPEL-0100-53-53-40-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-40/GP-AM-AMPEL-0100-53-53-40-10-000-MAN-A.md)  | MAN    |

#### 53‑50‑00 — Tail Cone Station <a name="ata‑53‑50‑00"></a>

| Doc ID         | Title                                          | File                                                                                                          | Type   |
| :------------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-50-00-000** | Tail Cone Structural Dwg (Empennage Int)(Ref ATA 55)| [GP-AM-AMPEL-0100-53-53-50-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-50/GP-AM-AMPEL-0100-53-53-50-00-000-DWG-A.md)  | DWG    |
| **53-50-10-000** | Tail Cone Repair Manual                      | [GP-AM-AMPEL-0100-53-53-50-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-50/GP-AM-AMPEL-0100-53-53-50-10-000-MAN-A.md)  | MAN    |

#### 53‑60‑00 — APU Compartment <a name="ata‑53‑60‑00"></a>

| Doc ID         | Title                                   | File                                                                                                          | Type   |
| :------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-60-00-000** | APU Compartment Structural Dwg (Ref ATA 49)| [GP-AM-AMPEL-0100-53-53-60-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-60/GP-AM-AMPEL-0100-53-53-60-00-000-DWG-A.md)  | DWG    |
| **53-60-10-000** | APU Compartment Repair Manual           | [GP-AM-AMPEL-0100-53-53-60-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-60/GP-AM-AMPEL-0100-53-53-60-10-000-MAN-A.md)  | MAN    |

#### 53‑70‑00 — Additional Stations (Reserved) <a name="ata‑53‑70‑00"></a>

| Doc ID         | Title                          | File                                                                                                          | Type   |
| :------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-70-00-000** | Reserved for Additional Stations | [GP-AM-AMPEL-0100-53-53-70-00-000-NOTE-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-70/GP-AM-AMPEL-0100-53-53-70-00-000-NOTE-A.md)| NOTE   |

#### 53‑80‑00 — Auxiliary Stations (Reserved) <a name="ata‑53‑80‑00"></a>

| Doc ID         | Title                         | File                                                                                                          | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **53-80-00-000** | Reserved for Auxiliary Stations | [GP-AM-AMPEL-0100-53-53-80-00-000-NOTE-A.md](./GP-AM/AMPEL_0100/ATA53_Fuselage/53-80/GP-AM-AMPEL-0100-53-53-80-00-000-NOTE-A.md)| NOTE   |

---
### ATA 54 — Nacelles/Pylons <a name="ata‑54"></a>

#### 54‑00‑00 — General <a name="ata‑54‑00‑00"></a>

| Doc ID         | Title                     | File                                                                                                          | Type     |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------ | :------- |
| **54-00-00-000** | Nacelle/Pylon Overview  | [GP-AM-AMPEL-0100-53-54-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA54_Nacelles/54-00/GP-AM-AMPEL-0100-53-54-00-00-000-OV-A.md)     | OV, SDD  |
| **54-00-00-001** | Design Specifications   | [GP-AM-AMPEL-0100-53-54-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA54_Nacelles/54-00/GP-AM-AMPEL-0100-53-54-00-00-001-SPEC-A.md) | SPEC     |

#### 54‑10‑00 — Nacelle Structure <a name="ata‑54‑10‑00"></a>

| Doc ID         | Title                             | File                                                                                                          | Type   |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **54-10-00-000** | Nacelle Structural Dwg (Ref ATA 71)| [GP-AM-AMPEL-0100-53-54-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA54_Nacelles/54-10/GP-AM-AMPEL-0100-53-54-10-00-000-DWG-A.md)  | DWG    |
| **54-10-10-000** | Nacelle Repair Manual           | [GP-AM-AMPEL-0100-53-54-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA54_Nacelles/54-10/GP-AM-AMPEL-0100-53-54-10-10-000-MAN-A.md)  | MAN    |

#### 54‑50‑00 — Pylon Structure <a name="ata‑54‑50‑00"></a>

| Doc ID         | Title                           | File                                                                                                          | Type   |
| :------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------ | :----- |
| **54-50-00-000** | Pylon Structural Dwg (Ref ATA 71)| [GP-AM-AMPEL-0100-53-54-50-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA54_Nacelles/54-50/GP-AM-AMPEL-0100-53-54-50-00-000-DWG-A.md)  | DWG    |
| **54-50-10-000** | Pylon Repair Manual             | [GP-AM-AMPEL-0100-53-54-50-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA54_Nacelles/54-50/GP-AM-AMPEL-0100-53-54-50-10-000-MAN-A.md)  | MAN    |

---
### ATA 55 — Stabilizers <a name="ata‑55"></a>

#### 55‑00‑00 — General <a name="ata‑55‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                              | Type     |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **55-00-00-000** | Stabilizer Overview     | [GP-AM-AMPEL-0100-53-55-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA55_Stabilizers/55-00/GP-AM-AMPEL-0100-53-55-00-00-000-OV-A.md)     | OV, SDD  |
| **55-00-00-001** | Design Specifications   | [GP-AM-AMPEL-0100-53-55-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA55_Stabilizers/55-00/GP-AM-AMPEL-0100-53-55-00-00-001-SPEC-A.md) | SPEC     |

#### 55‑10‑00 — Horizontal Stabilizer <a name="ata‑55‑10‑00"></a>

| Doc ID         | Title                                    | File                                                                                                              | Type   |
| :------------- | :--------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **55-10-00-000** | Horizontal Stabilizer Structural Dwg (Ref ATA 27)| [GP-AM-AMPEL-0100-53-55-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA55_Stabilizers/55-10/GP-AM-AMPEL-0100-53-55-10-00-000-DWG-A.md)  | DWG    |
| **55-10-10-000** | Horizontal Stabilizer Repair Manual    | [GP-AM-AMPEL-0100-53-55-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA55_Stabilizers/55-10/GP-AM-AMPEL-0100-53-55-10-10-000-MAN-A.md)  | MAN    |

#### 55‑30‑00 — Vertical Stabilizer <a name="ata‑55‑30‑00"></a>

| Doc ID         | Title                                    | File                                                                                                              | Type   |
| :------------- | :--------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **55-30-00-000** | Vertical Stabilizer Structural Dwg (Ref ATA 27)| [GP-AM-AMPEL-0100-53-55-30-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA55_Stabilizers/55-30/GP-AM-AMPEL-0100-53-55-30-00-000-DWG-A.md)  | DWG    |
| **55-30-10-000** | Vertical Stabilizer Repair Manual      | [GP-AM-AMPEL-0100-53-55-30-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA55_Stabilizers/55-30/GP-AM-AMPEL-0100-53-55-30-10-000-MAN-A.md)  | MAN    |

---
### ATA 56 — Windows <a name="ata‑56"></a>

#### 56‑00‑00 — General <a name="ata‑56‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                  | Type     |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **56-00-00-000** | Windows Overview        | [GP-AM-AMPEL-0100-53-56-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-00/GP-AM-AMPEL-0100-53-56-00-00-000-OV-A.md)       | OV, SDD  |
| **56-00-00-001** | Window Specifications   | [GP-AM-AMPEL-0100-53-56-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-00/GP-AM-AMPEL-0100-53-56-00-00-001-SPEC-A.md) | SPEC     |

#### 56‑10‑00 — Flight Compartment Windows <a name="ata‑56‑10‑00"></a>

| Doc ID         | Title                                      | File                                                                                                  | Type   |
| :------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **56-10-00-000** | Flight Compartment Window Spec           | [GP-AM-AMPEL-0100-53-56-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-10/GP-AM-AMPEL-0100-53-56-10-00-000-SPEC-A.md)| SPEC   |
| **56-10-10-000** | Flight Compartment Window Maint (Ref ATA 30)| [GP-AM-AMPEL-0100-53-56-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-10/GP-AM-AMPEL-0100-53-56-10-10-000-MAN-A.md)  | MAN    |

#### 56‑20‑00 — Passenger Compartment Windows <a name="ata‑56‑20‑00"></a>

| Doc ID         | Title                                   | File                                                                                                  | Type   |
| :------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **56-20-00-000** | Passenger Window Spec (Physical/VR)   | [GP-AM-AMPEL-0100-53-56-20-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-20/GP-AM-AMPEL-0100-53-56-20-00-000-SPEC-A.md)| SPEC   |
| **56-20-10-000** | VR Window System Int (Ref ATA 25, 44) | [GP-AM-AMPEL-0100-53-56-20-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-20/GP-AM-AMPEL-0100-53-56-20-10-000-SDD-A.md)    | SDD    |
| **56-20-20-000** | Passenger Window Maintenance          | [GP-AM-AMPEL-0100-53-56-20-20-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA56_Windows/56-20/GP-AM-AMPEL-0100-53-56-20-20-000-MAN-A.md)    | MAN    |

---
### ATA 57 — Wings <a name="ata‑57"></a>

#### 57‑00‑00 — General <a name="ata‑57‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                              | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------ | :------- |
| **57-00-00-000** | Wing Overview           | [GP-AM-AMPEL-0100-53-57-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-00/GP-AM-AMPEL-0100-53-57-00-00-000-OV-A.md)       | OV, SDD  |
| **57-00-00-001** | Wing Design Specs     | [GP-AM-AMPEL-0100-53-57-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-00/GP-AM-AMPEL-0100-53-57-00-00-001-SPEC-A.md) | SPEC     |

#### 57‑10‑00 — Wing Structure <a name="ata‑57‑10‑00"></a>

| Doc ID         | Title                                           | File                                                                                              | Type   |
| :------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **57-10-00-000** | Wing Structural Dwg (Box, Ribs, Spars)        | [GP-AM-AMPEL-0100-53-57-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-10/GP-AM-AMPEL-0100-53-57-10-00-000-DWG-A.md)  | DWG    |
| **57-10-10-000** | Wing Material Spec (Adv Composites)(Ref ATA 51)| [GP-AM-AMPEL-0100-53-57-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-10/GP-AM-AMPEL-0100-53-57-10-10-000-SPEC-A.md)| SPEC   |
| **57-10-20-000** | Wing Repair Manual                            | [GP-AM-AMPEL-0100-53-57-10-20-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-10/GP-AM-AMPEL-0100-53-57-10-20-000-MAN-A.md)  | MAN    |

#### 57‑40‑00 — Slat and Flap Systems <a name="ata‑57‑40‑00"></a>

| Doc ID         | Title                               | File                                                                                              | Type   |
| :------------- | :---------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **57-40-00-000** | High-Lift System Desc (Ref ATA 27)| [GP-AM-AMPEL-0100-53-57-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-40/GP-AM-AMPEL-0100-53-57-40-00-000-SDD-A.md)  | SDD    |
| **57-40-10-000** | Slat/Flap Maintenance Manual      | [GP-AM-AMPEL-0100-53-57-40-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-40/GP-AM-AMPEL-0100-53-57-40-10-000-MAN-A.md)  | MAN    |

#### 57‑50‑00 — Wing Folding <a name="ata‑57‑50‑00"></a>

| Doc ID         | Title                                 | File                                                                                              | Type   |
| :------------- | :------------------------------------ | :------------------------------------------------------------------------------------------------ | :----- |
| **57-50-00-000** | Wing Folding Mechanism Desc (If Appl) | [GP-AM-AMPEL-0100-53-57-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-50/GP-AM-AMPEL-0100-53-57-50-00-000-SDD-A.md)  | SDD    |
| **57-50-10-000** | Wing Folding Maintenance Manual       | [GP-AM-AMPEL-0100-53-57-50-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-50/GP-AM-AMPEL-0100-53-57-50-10-000-MAN-A.md)  | MAN    |

#### 57‑70‑00 — GPAM (GAIA Polymorphic Aero-Morphing) <a name="ata‑57‑70‑00"></a>

| Doc ID         | Title                                       | File                                                                                              | Type     |
| :------------- | :------------------------------------------ | :------------------------------------------------------------------------------------------------ | :------- |
| **57-70-00-000** | GPAM Structural Integration & Act (Ref ATA 27)| [GP-AM-AMPEL-0100-53-57-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-70/GP-AM-AMPEL-0100-53-57-70-00-000-SDD-A.md)    | SDD, ICD |
| **57-70-10-000** | GPAM Maintenance Manual                   | [GP-AM-AMPEL-0100-53-57-70-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA57_Wings/57-70/GP-AM-AMPEL-0100-53-57-70-10-000-MAN-A.md)    | MAN      |

---
### ATA 60 — Standard Practices – Engine <a name="ata‑60"></a>

#### 60‑00‑00 — General <a name="ata‑60‑00‑00"></a>

| Doc ID         | Title                             | File                                                                                                                    | Type   |
| :------------- | :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **60-00-00-000** | Engine Standard Practices Overview| [GP-AM-AMPEL-0100-53-60-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA60_EngineStdPract/60-00/GP-AM-AMPEL-0100-53-60-00-00-000-OV-A.md)   | OV     |
| **60-00-00-001** | General Standards               | [GP-AM-AMPEL-0100-53-60-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA60_EngineStdPract/60-00/GP-AM-AMPEL-0100-53-60-00-00-001-SPEC-A.md)| SPEC   |

#### 60‑10‑00 — Maintenance Procedures <a name="ata‑60‑10‑00"></a>

| Doc ID         | Title                                        | File                                                                                                                    | Type   |
| :------------- | :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **60-10-00-000** | Standard Engine Maint Procedures (Ref ATA 71-80)| [GP-AM-AMPEL-0100-53-60-10-00-000-PROC-A.md](./GP-AM/AMPEL_0100/ATA60_EngineStdPract/60-10/GP-AM-AMPEL-0100-53-60-10-00-000-PROC-A.md)| PROC   |

#### 60‑20‑00 — Testing Procedures <a name="ata‑60‑20‑00"></a>

| Doc ID         | Title                          | File                                                                                                                    | Type   |
| :------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **60-20-00-000** | Standard Engine Test Procedures| [GP-AM-AMPEL-0100-53-60-20-00-000-TEST-A.md](./GP-AM/AMPEL_0100/ATA60_EngineStdPract/60-20/GP-AM-AMPEL-0100-53-60-20-00-000-TEST-A.md)| TEST   |

---
### ATA 61 — Propellers/Propulsors (If Applicable) <a name="ata‑61"></a>

#### 61‑00‑00 — General <a name="ata‑61‑00‑00"></a>

| Doc ID         | Title                            | File                                                                                                              | Type     |
| :------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **61-00-00-000** | Propulsor System Ov (If Appl)  | [GP-AM-AMPEL-0100-53-61-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA61_Propulsors/61-00/GP-AM-AMPEL-0100-53-61-00-00-000-OV-A.md)     | OV, SDD  |
| **61-00-00-001** | System Specifications          | [GP-AM-AMPEL-0100-53-61-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA61_Propulsors/61-00/GP-AM-AMPEL-0100-53-61-00-00-001-SPEC-A.md) | SPEC     |

#### 61‑10‑00 — Blades <a name="ata‑61‑10‑00"></a>

| Doc ID         | Title                         | File                                                                                                              | Type   |
| :------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **61-10-00-000** | Blade Spec (Material, Geom) | [GP-AM-AMPEL-0100-53-61-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA61_Propulsors/61-10/GP-AM-AMPEL-0100-53-61-10-00-000-SPEC-A.md)| SPEC   |
| **61-10-10-000** | Blade Maintenance Manual    | [GP-AM-AMPEL-0100-53-61-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA61_Propulsors/61-10/GP-AM-AMPEL-0100-53-61-10-10-000-MAN-A.md)  | MAN    |

#### 61‑20‑00 — Control Systems <a name="ata‑61‑20‑00"></a>

| Doc ID         | Title                       | File                                                                                                              | Type   |
| :------------- | :-------------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **61-20-00-000** | Pitch Control System Desc   | [GP-AM-AMPEL-0100-53-61-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA61_Propulsors/61-20/GP-AM-AMPEL-0100-53-61-20-00-000-SDD-A.md)  | SDD    |
| **61-20-10-000** | Control System Spec       | [GP-AM-AMPEL-0100-53-61-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA61_Propulsors/61-20/GP-AM-AMPEL-0100-53-61-20-10-000-SPEC-A.md)| SPEC   |

---
### ATA 62–67 — Rotorcraft Specific (If Applicable) <a name="ata‑62"></a> <a name="ata‑63"></a> <a name="ata‑64"></a> <a name="ata‑65"></a> <a name="ata‑66"></a> <a name="ata‑67"></a>

*(Placeholder: Tables for ATA 62, 63, 64, 65, 66, 67 would be added here if the GP-AM platform included rotorcraft configurations. Currently marked as N/A or minimal)*

---
### ATA 71 — Power Plant – General <a name="ata‑71"></a>

#### 71‑00‑00 — General <a name="ata‑71‑00‑00"></a>

| Doc ID         | Title                              | File                                                                                                          | Type     |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------ | :------- |
| **71-00-00-000** | Power Plant Overview             | [GP-AM-AMPEL-0100-53-71-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-00/GP-AM-AMPEL-0100-53-71-00-00-000-OV-A.md)     | OV, SDD  |
| **71-00-00-001** | Power Plant Installation Specs   | [GP-AM-AMPEL-0100-53-71-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-00/GP-AM-AMPEL-0100-53-71-00-00-001-SPEC-A.md) | SPEC     |

#### 71‑10‑00 — Cowling <a name="ata‑71‑10‑00"></a>

| Doc ID         | Title                     | File                                                                                                          | Type     |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------ | :------- |
| **71-10-00-000** | Cowling Design and Access | [GP-AM-AMPEL-0100-53-71-10-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-10/GP-AM-AMPEL-0100-53-71-10-00-000-DWG-A.md)  | DWG, MAN |

#### 71‑20‑00 — Mounts <a name="ata‑71‑20‑00"></a>

| Doc ID         | Title                   | File                                                                                                          | Type   |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **71-20-00-000** | Engine Mount Spec     | [GP-AM-AMPEL-0100-53-71-20-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-20/GP-AM-AMPEL-0100-53-71-20-00-000-SPEC-A.md)| SPEC   |
| **71-20-10-000** | Engine Mount Maintenance| [GP-AM-AMPEL-0100-53-71-20-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-20/GP-AM-AMPEL-0100-53-71-20-10-000-MAN-A.md)  | MAN    |

#### 71‑50‑00 — Electric Propulsion Systems <a name="ata‑71‑50‑00"></a>

| Doc ID         | Title                               | File                                                                                                          | Type   |
| :------------- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **71-50-00-000** | Electric Motor Desc (If Appl)     | [GP-AM-AMPEL-0100-53-71-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-50/GP-AM-AMPEL-0100-53-71-50-00-000-SDD-A.md)    | SDD    |
| **71-50-10-000** | Electric Motor Specification      | [GP-AM-AMPEL-0100-53-71-50-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-50/GP-AM-AMPEL-0100-53-71-50-10-000-SPEC-A.md)| SPEC   |

#### 71‑60‑00 — Hybrid-Electric Systems <a name="ata‑71‑60‑00"></a>

| Doc ID         | Title                                          | File                                                                                                          | Type   |
| :------------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----- |
| **71-60-00-000** | Hybrid-Electric Arch Desc (Ref ATA 72, 71-50)| [GP-AM-AMPEL-0100-53-71-60-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-60/GP-AM-AMPEL-0100-53-71-60-00-000-SDD-A.md)    | SDD    |
| **71-60-10-000** | Hybrid System Specification                | [GP-AM-AMPEL-0100-53-71-60-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-60/GP-AM-AMPEL-0100-53-71-60-10-000-SPEC-A.md)| SPEC   |

#### 71‑70‑00 — Hydrogen Propulsion Systems <a name="ata‑71‑70‑00"></a>

| Doc ID         | Title                                             | File                                                                                                          | Type   |
| :------------- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------ | :----- |
| **71-70-00-000** | H2 Combustion Engine Desc (If Appl)(Ref ATA 72) | [GP-AM-AMPEL-0100-53-71-70-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-70/GP-AM-AMPEL-0100-53-71-70-00-000-SDD-A.md)    | SDD    |
| **71-70-10-000** | Hydrogen System Spec (Ref ATA 28, 85)           | [GP-AM-AMPEL-0100-53-71-70-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA71_PowerPlant/71-70/GP-AM-AMPEL-0100-53-71-70-10-000-SPEC-A.md)| SPEC   |

---
### ATA 72 — Engine (Turbine/Hybrid/H2) <a name="ata‑72"></a>

#### 72‑00‑00 — General <a name="ata‑72‑00‑00"></a>

| Doc ID         | Title                     | File                                                                                                | Type     |
| :------------- | :------------------------ | :-------------------------------------------------------------------------------------------------- | :------- |
| **72-00-00-000** | Engine Overview           | [GP-AM-AMPEL-0100-53-72-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-00/GP-AM-AMPEL-0100-53-72-00-00-000-OV-A.md)       | OV, SDD  |
| **72-00-00-001** | Engine Specifications     | [GP-AM-AMPEL-0100-53-72-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-00/GP-AM-AMPEL-0100-53-72-00-00-001-SPEC-A.md) | SPEC     |
| **72-00-00-002** | Engine Maintenance Manual | [GP-AM-AMPEL-0100-53-72-00-00-002-MAN-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-00/GP-AM-AMPEL-0100-53-72-00-00-002-MAN-A.md)  | MAN      |

#### 72‑30‑00 — Compressor <a name="ata‑72‑30‑00"></a>

| Doc ID         | Title                         | File                                                                                                | Type   |
| :------------- | :---------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **72-30-00-000** | Compressor Section Description| [GP-AM-AMPEL-0100-53-72-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-30/GP-AM-AMPEL-0100-53-72-30-00-000-SDD-A.md)  | SDD    |

#### 72‑40‑00 — Combustion Section <a name="ata‑72‑40‑00"></a>

| Doc ID         | Title                              | File                                                                                                | Type   |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **72-40-00-000** | Combustion Section Desc (SAF/H2) | [GP-AM-AMPEL-0100-53-72-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-40/GP-AM-AMPEL-0100-53-72-40-00-000-SDD-A.md)  | SDD    |

#### 72‑50‑00 — Turbine Section <a name="ata‑72‑50‑00"></a>

| Doc ID         | Title                      | File                                                                                                | Type   |
| :------------- | :------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **72-50-00-000** | Turbine Section Description| [GP-AM-AMPEL-0100-53-72-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-50/GP-AM-AMPEL-0100-53-72-50-00-000-SDD-A.md)  | SDD    |

#### 72‑Q01‑00 — Quantum Propulsion Extension <a name="ata‑72‑q01‑00"></a>

| Doc ID           | Title                                       | File                                                                                                    | Type     |
| :--------------- | :------------------------------------------ | :------------------------------------------------------------------------------------------------------ | :------- |
| **72-Q01-00-000**  | Quantum Propulsion Comp Desc (Ref GP-COM-QAO)| [GP-AM-AMPEL-0100-53-72-Q01-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-Q01/GP-AM-AMPEL-0100-53-72-Q01-00-000-SDD-A.md)    | SDD, SPEC|
| **72-Q01-00-001**  | Interface with Conventional Engine Sys    | [GP-AM-AMPEL-0100-53-72-Q01-00-001-ICD-A.md](./GP-AM/AMPEL_0100/ATA72_Engine/72-Q01/GP-AM-AMPEL-0100-53-72-Q01-00-001-ICD-A.md)    | ICD      |

---
### ATA 73 — Engine Fuel and Control <a name="ata‑73"></a>

#### 73‑00‑00 — General <a name="ata‑73‑00‑00"></a>

| Doc ID         | Title                            | File                                                                                                                    | Type     |
| :------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------- |
| **73-00-00-000** | Engine Fuel and Control Overview | [GP-AM-AMPEL-0100-53-73-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-00/GP-AM-AMPEL-0100-53-73-00-00-000-OV-A.md)     | OV, SDD  |
| **73-00-00-001** | System Specifications          | [GP-AM-AMPEL-0100-53-73-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-00/GP-AM-AMPEL-0100-53-73-00-00-001-SPEC-A.md) | SPEC     |

#### 73‑10‑00 — Fuel Delivery (Engine Side) <a name="ata‑73‑10‑00"></a>

| Doc ID         | Title                                     | File                                                                                                                    | Type   |
| :------------- | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----- |
| **73-10-00-000** | Engine Fuel Pump & Metering (Ref ATA 28)| [GP-AM-AMPEL-0100-53-73-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-10/GP-AM-AMPEL-0100-53-73-10-00-000-SDD-A.md)  | SDD    |
| **73-10-10-000** | Component Specs (H2/SAF Compatible)     | [GP-AM-AMPEL-0100-53-73-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-10/GP-AM-AMPEL-0100-53-73-10-10-000-SPEC-A.md)| SPEC   |

#### 73‑20‑00 — FADEC <a name="ata‑73‑20‑00"></a>

| Doc ID         | Title                                        | File                                                                                                                    | Type     |
| :------------- | :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------- |
| **73-20-00-000** | FADEC Description                          | [GP-AM-AMPEL-0100-53-73-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-20/GP-AM-AMPEL-0100-53-73-20-00-000-SDD-A.md)    | SDD      |
| **73-20-10-000** | FADEC Hardware & Software Spec             | [GP-AM-AMPEL-0100-53-73-20-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-20/GP-AM-AMPEL-0100-53-73-20-10-000-SPEC-A.md) | SPEC     |
| **73-20-20-000** | AI Engine Control Opt Algos (Ref GP-COM-AI)| [GP-AM-AMPEL-0100-53-73-20-20-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-20/GP-AM-AMPEL-0100-53-73-20-20-000-ALGO-A.md) | ALGO, SDD|
| **73-20-30-000** | FADEC to QAO Interface (Ref GP-COM-QAO)    | [GP-AM-AMPEL-0100-53-73-20-30-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA73_EngineFuelCtrl/73-20/GP-AM-AMPEL-0100-53-73-20-30-000-ICD-A.md)    | ICD      |

---
### ATA 74 — Ignition <a name="ata‑74"></a>

#### 74‑00‑00 — General <a name="ata‑74‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                | Type     |
| :------------- | :---------------------- | :-------------------------------------------------------------------------------------------------- | :------- |
| **74-00-00-000** | Ignition System Overview| [GP-AM-AMPEL-0100-53-74-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA74_Ignition/74-00/GP-AM-AMPEL-0100-53-74-00-00-000-OV-A.md)     | OV, SDD  |
| **74-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-74-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA74_Ignition/74-00/GP-AM-AMPEL-0100-53-74-00-00-001-SPEC-A.md) | SPEC     |

#### 74‑10‑00 — Exciter and Leads <a name="ata‑74‑10‑00"></a>

| Doc ID         | Title                        | File                                                                                                | Type   |
| :------------- | :--------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **74-10-00-000** | Exciter Unit and Lead Spec | [GP-AM-AMPEL-0100-53-74-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA74_Ignition/74-10/GP-AM-AMPEL-0100-53-74-10-00-000-SPEC-A.md)| SPEC   |

#### 74‑30‑00 — Igniter Plugs <a name="ata‑74‑30‑00"></a>

| Doc ID         | Title                              | File                                                                                                | Type   |
| :------------- | :--------------------------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **74-30-00-000** | Igniter Plug Spec (H2 Compatible)| [GP-AM-AMPEL-0100-53-74-30-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA74_Ignition/74-30/GP-AM-AMPEL-0100-53-74-30-00-000-SPEC-A.md)| SPEC   |

---
### ATA 75 — Air (Engine Bleed/ECS Input) <a name="ata‑75"></a>

#### 75‑00‑00 — General <a name="ata‑75‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                      | Type     |
| :------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------- | :------- |
| **75-00-00-000** | Engine Air System Overview| [GP-AM-AMPEL-0100-53-75-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA75_EngineAir/75-00/GP-AM-AMPEL-0100-53-75-00-00-000-OV-A.md)     | OV, SDD  |
| **75-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-75-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA75_EngineAir/75-00/GP-AM-AMPEL-0100-53-75-00-00-001-SPEC-A.md) | SPEC     |

#### 75‑10‑00 — Anti-Ice <a name="ata‑75‑10‑00"></a>

| Doc ID         | Title                                | File                                                                                                      | Type   |
| :------------- | :----------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **75-10-00-000** | Engine Anti-Ice System (Ref ATA 30)| [GP-AM-AMPEL-0100-53-75-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA75_EngineAir/75-10/GP-AM-AMPEL-0100-53-75-10-00-000-SDD-A.md)  | SDD    |

#### 75‑30‑00 — Ducting and Valves <a name="ata‑75‑30‑00"></a>

| Doc ID         | Title                             | File                                                                                                      | Type   |
| :------------- | :-------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **75-30-00-000** | Bleed Air Ducting Dwg (Ref ATA 36)| [GP-AM-AMPEL-0100-53-75-30-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA75_EngineAir/75-30/GP-AM-AMPEL-0100-53-75-30-00-000-DWG-A.md)  | DWG    |
| **75-30-10-000** | Valve Specifications            | [GP-AM-AMPEL-0100-53-75-30-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA75_EngineAir/75-30/GP-AM-AMPEL-0100-53-75-30-10-000-SPEC-A.md)| SPEC   |

---
### ATA 76 — Engine Controls <a name="ata‑76"></a>

#### 76‑00‑00 — General <a name="ata‑76‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                                | Type     |
| :------------- | :---------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **76-00-00-000** | Engine Controls Overview| [GP-AM-AMPEL-0100-53-76-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA76_EngineControls/76-00/GP-AM-AMPEL-0100-53-76-00-00-000-OV-A.md)     | OV, SDD  |
| **76-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-76-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA76_EngineControls/76-00/GP-AM-AMPEL-0100-53-76-00-00-001-SPEC-A.md) | SPEC     |

#### 76‑10‑00 — Thrust/Power Lever <a name="ata‑76‑10‑00"></a>

| Doc ID         | Title                                   | File                                                                                                                | Type   |
| :------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **76-10-00-000** | Thrust/Power Lever Desc (Ref ATA 22)  | [GP-AM-AMPEL-0100-53-76-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA76_EngineControls/76-10/GP-AM-AMPEL-0100-53-76-10-00-000-SDD-A.md)  | SDD    |
| **76-10-10-000** | Interface with FADEC (Ref ATA 73)     | [GP-AM-AMPEL-0100-53-76-10-10-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA76_EngineControls/76-10/GP-AM-AMPEL-0100-53-76-10-10-000-ICD-A.md)  | ICD    |

#### 76‑20‑00 — Emergency Shutdown <a name="ata‑76‑20‑00"></a>

| Doc ID         | Title                     | File                                                                                                                | Type   |
| :------------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **76-20-00-000** | Emergency Shutdown System | [GP-AM-AMPEL-0100-53-76-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA76_EngineControls/76-20/GP-AM-AMPEL-0100-53-76-20-00-000-SDD-A.md)  | SDD    |

---
### ATA 77 — Engine Indication <a name="ata‑77"></a>

#### 77‑00‑00 — General <a name="ata‑77‑00‑00"></a>

| Doc ID         | Title                       | File                                                                                                      | Type     |
| :------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------- | :------- |
| **77-00-00-000** | Engine Indication Overview  | [GP-AM-AMPEL-0100-53-77-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-00/GP-AM-AMPEL-0100-53-77-00-00-000-OV-A.md)       | OV, SDD  |
| **77-00-00-001** | System Specifications       | [GP-AM-AMPEL-0100-53-77-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-00/GP-AM-AMPEL-0100-53-77-00-00-001-SPEC-A.md) | SPEC     |

#### 77‑10‑00 — Thrust/Power Indication <a name="ata‑77‑10‑00"></a>

| Doc ID         | Title                                    | File                                                                                                      | Type   |
| :------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **77-10-00-000** | Primary Engine Param Display (Ref ATA 31)| [GP-AM-AMPEL-0100-53-77-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-10/GP-AM-AMPEL-0100-53-77-10-00-000-SDD-A.md)  | SDD    |

#### 77‑20‑00 — Temperature Monitoring <a name="ata‑77‑20‑00"></a>

| Doc ID         | Title                                    | File                                                                                                      | Type   |
| :------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **77-20-00-000** | Temperature Indication Sys (EGT, CHT)  | [GP-AM-AMPEL-0100-53-77-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-20/GP-AM-AMPEL-0100-53-77-20-00-000-SDD-A.md)  | SDD    |

#### 77‑30‑00 — Vibration Monitoring <a name="ata‑77‑30‑00"></a>

| Doc ID         | Title                                    | File                                                                                                      | Type   |
| :------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **77-30-00-000** | Vibration Monitoring Sys Desc (Ref ATA 18)| [GP-AM-AMPEL-0100-53-77-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-30/GP-AM-AMPEL-0100-53-77-30-00-000-SDD-A.md)  | SDD    |

#### 77‑40‑00 — AI Health Monitoring <a name="ata‑77‑40‑00"></a>

| Doc ID         | Title                                           | File                                                                                                      | Type   |
| :------------- | :---------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----- |
| **77-40-00-000** | AI Engine Health Mon Sys Desc (Ref GP-COM-AI, ATA 45)| [GP-AM-AMPEL-0100-53-77-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-40/GP-AM-AMPEL-0100-53-77-40-00-000-SDD-A.md)    | SDD    |
| **77-40-10-000** | Prognostic Algorithms                         | [GP-AM-AMPEL-0100-53-77-40-10-000-ALGO-A.md](./GP-AM/AMPEL_0100/ATA77_EngineInd/77-40/GP-AM-AMPEL-0100-53-77-40-10-000-ALGO-A.md)| ALGO   |

---
### ATA 78 — Exhaust <a name="ata‑78"></a>

#### 78‑00‑00 — General <a name="ata‑78‑00‑00"></a>

| Doc ID         | Title                                     | File                                                                                                  | Type     |
| :------------- | :---------------------------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **78-00-00-000** | Exhaust System Overview                 | [GP-AM-AMPEL-0100-53-78-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA78_Exhaust/78-00/GP-AM-AMPEL-0100-53-78-00-00-000-OV-A.md)     | OV, SDD  |
| **78-00-00-001** | Sys Specs (Noise/Emissions)(Ref ATA 18) | [GP-AM-AMPEL-0100-53-78-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA78_Exhaust/78-00/GP-AM-AMPEL-0100-53-78-00-00-001-SPEC-A.md) | SPEC     |

#### 78‑10‑00 — Collector/Nozzle <a name="ata‑78‑10‑00"></a>

| Doc ID         | Title                      | File                                                                                                  | Type   |
| :------------- | :------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **78-10-00-000** | Exhaust Nozzle Description | [GP-AM-AMPEL-0100-53-78-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA78_Exhaust/78-10/GP-AM-AMPEL-0100-53-78-10-00-000-SDD-A.md)  | SDD    |
| **78-10-10-000** | Exhaust Nozzle Maintenance | [GP-AM-AMPEL-0100-53-78-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA78_Exhaust/78-10/GP-AM-AMPEL-0100-53-78-10-10-000-MAN-A.md)  | MAN    |

#### 78‑30‑00 — Thrust Reverser <a name="ata‑78‑30‑00"></a>

| Doc ID         | Title                                 | File                                                                                                  | Type   |
| :------------- | :------------------------------------ | :---------------------------------------------------------------------------------------------------- | :----- |
| **78-30-00-000** | Thrust Reverser System Desc (If Appl) | [GP-AM-AMPEL-0100-53-78-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA78_Exhaust/78-30/GP-AM-AMPEL-0100-53-78-30-00-000-SDD-A.md)  | SDD    |
| **78-30-10-000** | Thrust Reverser Maintenance Manual    | [GP-AM-AMPEL-0100-53-78-30-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA78_Exhaust/78-30/GP-AM-AMPEL-0100-53-78-30-10-000-MAN-A.md)  | MAN    |

---
### ATA 79 — Oil <a name="ata‑79"></a>

#### 79‑00‑00 — General <a name="ata‑79‑00‑00"></a>

| Doc ID         | Title                                     | File                                                                                              | Type     |
| :------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------ | :------- |
| **79-00-00-000** | Oil System Overview                     | [GP-AM-AMPEL-0100-53-79-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA79_Oil/79-00/GP-AM-AMPEL-0100-53-79-00-00-000-OV-A.md)       | OV, SDD  |
| **79-00-00-001** | Sys Specs (incl. Sustainable Oils)      | [GP-AM-AMPEL-0100-53-79-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA79_Oil/79-00/GP-AM-AMPEL-0100-53-79-00-00-001-SPEC-A.md) | SPEC     |

#### 79‑10‑00 — Storage <a name="ata‑79‑10‑00"></a>

| Doc ID         | Title                 | File                                                                                              | Type   |
| :------------- | :-------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **79-10-00-000** | Oil Tank Specification| [GP-AM-AMPEL-0100-53-79-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA79_Oil/79-10/GP-AM-AMPEL-0100-53-79-10-00-000-SPEC-A.md)| SPEC   |

#### 79‑20‑00 — Distribution <a name="ata‑79‑20‑00"></a>

| Doc ID         | Title                                     | File                                                                                              | Type   |
| :------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------ | :----- |
| **79-20-00-000** | Oil Distribution Sys (Pumps, Filters, Coolers)| [GP-AM-AMPEL-0100-53-79-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA79_Oil/79-20/GP-AM-AMPEL-0100-53-79-20-00-000-SDD-A.md)    | SDD    |

#### 79‑30‑00 — Indicating <a name="ata‑79‑30‑00"></a>

| Doc ID         | Title                                       | File                                                                                              | Type   |
| :------------- | :------------------------------------------ | :------------------------------------------------------------------------------------------------ | :----- |
| **79-30-00-000** | Oil Indication Sys (Press/Temp/Qty)(Ref ATA 77)| [GP-AM-AMPEL-0100-53-79-30-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA79_Oil/79-30/GP-AM-AMPEL-0100-53-79-30-00-000-SDD-A.md)    | SDD    |

---
### ATA 80 — Starting <a name="ata‑80"></a>

#### 80‑00‑00 — General <a name="ata‑80‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                  | Type     |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **80-00-00-000** | Starting System Overview| [GP-AM-AMPEL-0100-53-80-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA80_Starting/80-00/GP-AM-AMPEL-0100-53-80-00-00-000-OV-A.md)     | OV, SDD  |
| **80-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-80-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA80_Starting/80-00/GP-AM-AMPEL-0100-53-80-00-00-001-SPEC-A.md) | SPEC     |

#### 80‑10‑00 — Cranking <a name="ata‑80‑10‑00"></a>

| Doc ID         | Title                                | File                                                                                                  | Type   |
| :------------- | :----------------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **80-10-00-000** | Starter Desc (Electric/Air Turbine)| [GP-AM-AMPEL-0100-53-80-10-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA80_Starting/80-10/GP-AM-AMPEL-0100-53-80-10-00-000-SDD-A.md)  | SDD    |
| **80-10-10-000** | Starter Specification              | [GP-AM-AMPEL-0100-53-80-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA80_Starting/80-10/GP-AM-AMPEL-0100-53-80-10-10-000-SPEC-A.md)| SPEC   |

#### 80‑20‑00 — Ignition <a name="ata‑80‑20‑00"></a>

| Doc ID         | Title                          | File                                                                                                  | Type   |
| :------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **80-20-00-000** | Reference to Ignition Sys (ATA 74)| [GP-AM-AMPEL-0100-53-80-20-00-000-REF-A.md](./GP-AM/AMPEL_0100/ATA80_Starting/80-20/GP-AM-AMPEL-0100-53-80-20-00-000-REF-A.md) | REF    |

---
### ATA 81 — Turbines (Reciprocating Engines) <a name="ata‑81"></a>

#### 81‑00‑00 — General <a name="ata‑81‑00‑00"></a>

| Doc ID         | Title                         | File                                                                                                                | Type   |
| :------------- | :---------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **81-00-00-000** | Chapter Likely Not Applicable | [GP-AM-AMPEL-0100-53-81-00-00-000-NOTE-A.md](./GP-AM/AMPEL_0100/ATA81_RecipTurbine/81-00/GP-AM-AMPEL-0100-53-81-00-00-000-NOTE-A.md)| NOTE   |

---
### ATA 82 — Water Injection <a name="ata‑82"></a>

#### 82‑00‑00 — General <a name="ata‑82‑00‑00"></a>

| Doc ID         | Title                              | File                                                                                                                | Type     |
| :------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **82-00-00-000** | Water Injection Sys Ov (If Appl) | [GP-AM-AMPEL-0100-53-82-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA82_WaterInjection/82-00/GP-AM-AMPEL-0100-53-82-00-00-000-OV-A.md)   | OV, SDD  |
| **82-00-00-001** | System Specifications            | [GP-AM-AMPEL-0100-53-82-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA82_WaterInjection/82-00/GP-AM-AMPEL-0100-53-82-00-00-001-SPEC-A.md)| SPEC     |

---
### ATA 83 — Accessory Gear Boxes <a name="ata‑83"></a>

#### 83‑00‑00 — General <a name="ata‑83‑00‑00"></a>

| Doc ID         | Title                     | File                                                                                                              | Type     |
| :------------- | :------------------------ | :---------------------------------------------------------------------------------------------------------------- | :------- |
| **83-00-00-000** | Accessory Gearbox Overview| [GP-AM-AMPEL-0100-53-83-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA83_AccessoryGB/83-00/GP-AM-AMPEL-0100-53-83-00-00-000-OV-A.md)     | OV, SDD  |
| **83-00-00-001** | System Specifications     | [GP-AM-AMPEL-0100-53-83-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA83_AccessoryGB/83-00/GP-AM-AMPEL-0100-53-83-00-00-001-SPEC-A.md) | SPEC     |

#### 83‑10‑00 — Drive Shaft <a name="ata‑83‑10‑00"></a>

| Doc ID         | Title                  | File                                                                                                              | Type   |
| :------------- | :--------------------- | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **83-10-00-000** | Drive Shaft Specification| [GP-AM-AMPEL-0100-53-83-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA83_AccessoryGB/83-10/GP-AM-AMPEL-0100-53-83-10-00-000-SPEC-A.md)| SPEC   |

#### 83‑20‑00 — Gearbox Assembly <a name="ata‑83‑20‑00"></a>

| Doc ID         | Title                     | File                                                                                                              | Type   |
| :------------- | :------------------------ | :---------------------------------------------------------------------------------------------------------------- | :----- |
| **83-20-00-000** | Gearbox Assembly Drawing  | [GP-AM-AMPEL-0100-53-83-20-00-000-DWG-A.md](./GP-AM/AMPEL_0100/ATA83_AccessoryGB/83-20/GP-AM-AMPEL-0100-53-83-20-00-000-DWG-A.md)  | DWG    |
| **83-20-10-000** | Gearbox Maintenance Manual| [GP-AM-AMPEL-0100-53-83-20-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA83_AccessoryGB/83-20/GP-AM-AMPEL-0100-53-83-20-10-000-MAN-A.md)  | MAN    |

---
### ATA 84 — Reserved for Future Use <a name="ata‑84"></a>

#### 84‑00‑00 — General <a name="ata‑84‑00‑00"></a>

| Doc ID         | Title           | File                                                                                                        | Type   |
| :------------- | :-------------- | :---------------------------------------------------------------------------------------------------------- | :----- |
| **84-00-00-000** | Chapter Reserved| [GP-AM-AMPEL-0100-53-84-00-00-000-NOTE-A.md](./GP-AM/AMPEL_0100/ATA84_Reserved/84-00/GP-AM-AMPEL-0100-53-84-00-00-000-NOTE-A.md)| NOTE   |

---
### ATA 85 — Fuel Cell System <a name="ata‑85"></a>

#### 85‑00‑00 — General <a name="ata‑85‑00‑00"></a>

| Doc ID         | Title                   | File                                                                                                  | Type     |
| :------------- | :---------------------- | :---------------------------------------------------------------------------------------------------- | :------- |
| **85-00-00-000** | Fuel Cell System Ov     | [GP-AM-AMPEL-0100-53-85-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA85_FuelCell/85-00/GP-AM-AMPEL-0100-53-85-00-00-000-OV-A.md)     | OV, SDD  |
| **85-00-00-001** | System Specifications   | [GP-AM-AMPEL-0100-53-85-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA85_FuelCell/85-00/GP-AM-AMPEL-0100-53-85-00-00-001-SPEC-A.md) | SPEC     |

#### 85‑10‑00 — Fuel Cell Stack <a name="ata‑85‑10‑00"></a>

| Doc ID         | Title                    | File                                                                                                  | Type   |
| :------------- | :----------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **85-10-00-000** | Fuel Cell Stack Spec   | [GP-AM-AMPEL-0100-53-85-10-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA85_FuelCell/85-10/GP-AM-AMPEL-0100-53-85-10-00-000-SPEC-A.md)| SPEC   |
| **85-10-10-000** | Stack Maintenance Manual | [GP-AM-AMPEL-0100-53-85-10-10-000-MAN-A.md](./GP-AM/AMPEL_0100/ATA85_FuelCell/85-10/GP-AM-AMPEL-0100-53-85-10-10-000-MAN-A.md)  | MAN    |

#### 85‑20‑00 — Hydrogen Processor <a name="ata‑85‑20‑00"></a>

| Doc ID         | Title                                   | File                                                                                                  | Type   |
| :------------- | :-------------------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **85-20-00-000** | Hydrogen Supply & Processing (Ref ATA 28)| [GP-AM-AMPEL-0100-53-85-20-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA85_FuelCell/85-20/GP-AM-AMPEL-0100-53-85-20-00-000-SDD-A.md)    | SDD    |

#### 85‑30‑00 — Power Conditioning <a name="ata‑85‑30‑00"></a>

| Doc ID         | Title                                    | File                                                                                                  | Type   |
| :------------- | :--------------------------------------- | :---------------------------------------------------------------------------------------------------- | :----- |
| **85-30-00-000** | Power Conditioning Unit Spec (Ref ATA 24)| [GP-AM-AMPEL-0100-53-85-30-00-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA85_FuelCell/85-30/GP-AM-AMPEL-0100-53-85-30-00-000-SPEC-A.md)| SPEC   |

---
### ATA 91 — Charts <a name="ata‑91"></a>

#### 91‑00‑00 — General <a name="ata‑91‑00‑00"></a>

| Doc ID         | Title           | File                                                                                                | Type   |
| :------------- | :-------------- | :-------------------------------------------------------------------------------------------------- | :----- |
| **91-00-00-000** | Charts Overview | [GP-AM-AMPEL-0100-53-91-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA91_Charts/91-00/GP-AM-AMPEL-0100-53-91-00-00-000-OV-A.md)       | OV     |
| **91-00-00-001** | Chart Index     | [GP-AM-AMPEL-0100-53-91-00-00-001-IDX-A.md](./GP-AM/AMPEL_0100/ATA91_Charts/91-00/GP-AM-AMPEL-0100-53-91-00-00-001-IDX-A.md)    | IDX    |

---
### ATA 92 — Electrical System Installation <a name="ata‑92"></a>

#### 92‑00‑00 — General <a name="ata‑92‑00‑00"></a>

| Doc ID         | Title                                         | File                                                                                                                | Type     |
| :------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :------- |
| **92-00-00-000** | Electrical Installation Overview              | [GP-AM-AMPEL-0100-53-92-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA92_ElecInstall/92-00/GP-AM-AMPEL-0100-53-92-00-00-000-OV-A.md)     | OV       |
| **92-00-00-001** | Standard Wiring Install Practices (Ref ATA 20)| [GP-AM-AMPEL-0100-53-92-00-00-001-PROC-A.md](./GP-AM/AMPEL_0100/ATA92_ElecInstall/92-00/GP-AM-AMPEL-0100-53-92-00-00-001-PROC-A.md) | PROC     |
| **92-00-00-002** | Wiring Installation Drawings Index          | [GP-AM-AMPEL-0100-53-92-00-00-002-DWG-A.md](./GP-AM/AMPEL_0100/ATA92_ElecInstall/92-00/GP-AM-AMPEL-0100-53-92-00-00-002-DWG-A.md)    | DWG, IDX |

---
### ATA 95 — Special Equipment (GSE) <a name="ata‑95"></a>

#### 95‑00‑00 — General <a name="ata‑95‑00‑00"></a>

| Doc ID         | Title                               | File                                                                                                                | Type       |
| :------------- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :--------- |
| **95-00-00-000** | Special Equipment Overview        | [GP-AM-AMPEL-0100-53-95-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA95_SpecialEquip/95-00/GP-AM-AMPEL-0100-53-95-00-00-000-OV-A.md)     | OV         |
| **95-00-00-001** | Special GSE List (Ref GP-GRO)     | [GP-AM-AMPEL-0100-53-95-00-00-001-LIST-A.md](./GP-AM/AMPEL_0100/ATA95_SpecialEquip/95-00/GP-AM-AMPEL-0100-53-95-00-00-001-LIST-A.md)| LIST, SPEC |

---
### ATA 97 — Wiring Reporting <a name="ata‑97"></a>

#### 97‑00‑00 — General <a name="ata‑97‑00‑00"></a>

| Doc ID         | Title                        | File                                                                                                                | Type       |
| :------------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------ | :--------- |
| **97-00-00-000** | Wiring Reporting Overview    | [GP-AM-AMPEL-0100-53-97-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA97_WiringReport/97-00/GP-AM-AMPEL-0100-53-97-00-00-000-OV-A.md)     | OV         |
| **97-00-00-001** | Wiring Data Standards (EWIS) | [GP-AM-AMPEL-0100-53-97-00-00-001-SPEC-A.md](./GP-AM/AMPEL_0100/ATA97_WiringReport/97-00/GP-AM-AMPEL-0100-53-97-00-00-001-SPEC-A.md)| SPEC       |
| **97-00-00-002** | Wiring List Index            | [GP-AM-AMPEL-0100-53-97-00-00-002-LIST-A.md](./GP-AM/AMPEL_0100/ATA97_WiringReport/97-00/GP-AM-AMPEL-0100-53-97-00-00-002-LIST-A.md)| LIST, IDX  |

---
### ATA 99 — Special / Emerging Tech <a name="ata‑99"></a>

#### 99‑00‑00 — General <a name="ata‑99‑00‑00"></a>

| Doc ID         | Title                               | File                                                                                                                | Type   |
| :------------- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-00-00-000** | Special/Emerging Technologies Ov  | [GP-AM-AMPEL-0100-53-99-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-00/GP-AM-AMPEL-0100-53-99-00-00-000-OV-A.md)     | OV     |
| **99-00-00-001** | Placeholder for Future Systems    | [GP-AM-AMPEL-0100-53-99-00-00-001-NOTE-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-00/GP-AM-AMPEL-0100-53-99-00-00-001-NOTE-A.md) | NOTE   |

---
### ATA 99 — Special / Emerging Tech <a name="ata‑99"></a>

#### 99‑00‑00 — General <a name="ata‑99‑00‑00"></a>

| Doc ID         | Title                               | File                                                                                                                | Type   |
| :------------- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-00-00-000** | Special/Emerging Technologies Ov  | [GP-AM-AMPEL-0100-53-99-00-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-00/GP-AM-AMPEL-0100-53-99-00-00-000-OV-A.md)     | OV     |
| **99-00-00-001** | Placeholder for Future Systems    | [GP-AM-AMPEL-0100-53-99-00-00-001-NOTE-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-00/GP-AM-AMPEL-0100-53-99-00-00-001-NOTE-A.md) | NOTE   |

---

#### 99‑10‑00 — Advanced Sensor Systems <a name="ata‑99‑10‑00"></a>

| Doc ID         | Title                                           | File                                                                                                                | Type   |
| :------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-10-00-000** | Novel Sensor Technologies Ov (Ref ATA 31)     | [GP-AM-AMPEL-0100-53-99-10-00-000-OV-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-10/GP-AM-AMPEL-0100-53-99-10-00-000-OV-A.md)     | OV     |
| **99-10-10-000** | LiDAR/Env Sensor Specifications               | [GP-AM-AMPEL-0100-53-99-10-10-000-SPEC-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-10/GP-AM-AMPEL-0100-53-99-10-10-000-SPEC-A.md) | SPEC   |

---

#### 99‑20‑00 — Novel Materials Reports <a name="ata‑99‑20‑00"></a>

| Doc ID         | Title                                           | File                                                                                                                | Type   |
| :------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-20-00-000** | AMPEL/Metamaterial Application Rpt (Ref ATA 51) | [GP-AM-AMPEL-0100-53-99-20-00-000-RPT-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-20/GP-AM-AMPEL-0100-53-99-20-00-000-RPT-A.md) | RPT    |

---

#### 99‑30‑00 — RAME Integration <a name="ata‑99‑30‑00"></a>

| Doc ID         | Title                                         | File                                                                                                                | Type   |
| :------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-30-00-000** | Robotic Aircraft Maintenance Env (Ref GP-GRO) | [GP-AM-AMPEL-0100-53-99-30-00-000-ICD-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-30/GP-AM-AMPEL-0100-53-99-30-00-000-ICD-A.md) | ICD    |

---

#### 99‑40‑00 — Energy Management Systems <a name="ata‑99‑40‑00"></a>

| Doc ID         | Title                                             | File                                                                                                                | Type   |
| :------------- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-40-00-000** | Aircraft-Wide Energy Opt (Ref ATA 24, 71)        | [GP-AM-AMPEL-0100-53-99-40-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-40/GP-AM-AMPEL-0100-53-99-40-00-000-SDD-A.md) | SDD    |

---

#### 99‑50‑00 — Emissions Monitoring and Reduction <a name="ata‑99‑50‑00"></a>

| Doc ID         | Title                                         | File                                                                                                                | Type   |
| :------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----- |
| **99-50-00-000** | Real-Time Emissions Mon Sys (Ref ATA 78)    | [GP-AM-AMPEL-0100-53-99-50-00-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-50/GP-AM-AMPEL-0100-53-99-50-00-000-SDD-A.md) | SDD    |
| **99-50-10-000** | Carbon Capture System Desc (Ref ATA 78)     | [GP-AM-AMPEL-0100-53-99-50-10-000-SDD-A.md](./GP-AM/AMPEL_0100/ATA99_EmergingTech/99-50/GP-AM-AMPEL-0100-53-99-50-10-000-SDD-A.md) | SDD    |


This completes the reformatted ATA 00-99 breakdown using the specified table structure.
