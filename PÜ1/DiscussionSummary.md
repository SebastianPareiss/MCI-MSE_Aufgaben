## Project background

### Purpose of project

Generating software with the goal to extract EKG monitor data from a bicycle ergometer. The data should be analyzed and visualized on a display. This project should teach us how to work on bigger projects further down our studies. The goal of this project is to increase our programming skills and to give us experience working as a team.
### Scope of project

The project consists of several different tasks. Starting with a planning phase, consisting of a a "Readme", a "discussion Summary", going into actually codeing and implementing of operations fit to display EKG-data. A rigorous documentary process is parallely done.
### Other background information

This project has been developed for educational purposes only at the MCI Innsbruck. It might not be used otherwise. Developers take no responsibillity if mal-used.

## Perspectives
### Who will use the system?

Potentially, beside us in form of a lecture assingend project, anyone in need of EKG-testing and survailance. In this case specifically a company selling bicycle-ergometers.

### Who can provide input about the system?

Input may come from: us, the developers, and our lectures. Additional help from outside may contribute.


## Project Objectives
### Known business rules

Get paied before delivering? We find ourselves with a lack of background information to properly adress this point.

### System information and/or diagrams

![](ekg_example.png)

### Assumptions and dependencies

EKG example.png is assumed to be correct within a resonable margin of error. The hardware must work as planned so the software can use the provided data. The whole analysing process depends on the functionality of the programmed software.

Task 2:

Information in the data:

There are 3 different data sets for each test person. On the one hand, a large amount of ECG data from the test subjects are shown.
The next data set shows the performance over time. The test lasted 180s. The fluctuations in the performance provided by the test persons are therefore shown.
A distinction is made between personal description, year of birth, duration and difficulty of the test.

Temporal resolution of the data and duration of the test:

The performance test has a duration of 180s, i.e. 3 minutes.
The data indicate the performance achieved in every single second of the test.
The data will probably be evaluated later on based on the personal data of the test persons (age).

### Design and implementation constraints

The hardware of the bicycle ergometer is limited, for example the number of displays to show data.
Storage place and processing power are limited as well and shall be restrained to a reasonable level. Visual output must be interpretable by a diagnostician.

## Risks

Possible sources of error might be the data gathering process. Also the analysing and visualisation of the measurements could lead to errors. The hardware must also work, otherwise the software cannot be used properly. 

## Known future enhancements

None as of now

## References

https://github.com/jhumci/MCI-MSE_Aufgaben

## Open, unresolved or TBD issues

Writing and implementing the code.
Testing of functionallity.
Implement further enhancments if necesarry.
