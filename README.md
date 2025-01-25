
# SimPy: NHS waiting game - bust the list

![Image](https://github.com/OmdenaAI/london-chapter-nlp-self-harm/blob/main/src/visualizations/Promo_London_chapter.png)

Today in London, the average referral to treatment waiting time is [insert]. This doesn't include the time people wait for a basic diagnostic test. In this simulation game, players are challenged to bust their local hospital diagnostic waiting list. You're a local NHS leader, and a supermarket has loaned their car park facilities. You have 6-weeks to bust the list before you go broke.  

## Contribution Guidelines
- Have a look at the [project structure](#project-structure) and [folder overview](#folder-overview) below to understand where to store/upload your contribution;
- If you're creating a task, go to the task folder and create a new folder with the below naming convention and add a README.md with task details and goals to help other contributors understand;
    - Task Folder Naming Convention : _task-n-taskname.(n is the task number)_  ex: task-1-data-analysis, task-2-model-deployment etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relevant location and update the README.md information table with your contribution details;
- Make sure your files (jupyter notebooks, python files, data sheet file names etc) have proper naming to help others in easily identifing them;
- Please restrict yourself from creating unnecessary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion. 

## Project Structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers/collaborators using this project.
    ├── original           <- Original Source Code of the challenge hosted by HygeiaOrg. Can be used as a reference code for the current project goal.
    │ 
    │
    ├── reports            <- Folder containing the final reports/results of this project
    │   └── README.md      <- Details about final reports and analysis
    │ 
    │   
    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        ├── visualizations <- Code and visualization dashboards generated for the project
        │
        └── results        <- Folder to store final analysis and modelling results and code.
--------

## Folder Overview

- Original          - Folder containing old/completed challenge code.
- Reports           - Folder to store all Final Reports of this project.
- Data              - Folder to Store all the data collected and used for this project. 
- Docs              - Folder for task documentation, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referenced code/research papers and other useful documents used for this project.
- Tasks             - Master folder for all tasks.
  - All Task Folder names should follow specific naming conventions.
  - All Task folder names should be in chronological order (from 1 to n).
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information.
  - Update the [task-table](./src/tasks/README.md#task-table) whenever a task is created and explain the purpose and goals of the task to others.
- Visualization     - Folder to store dashboards, analysis and visualization reports.
- Results           - Folder to store final analysis modelling results for the project.


## Project Setup
Get started with Git (https://codecademy.com/article/what-is-git-and-github-desktop)

Open the Command line or Terminal

- Clone the repository:
```
git clone https://github.com/HygeiaOrg/NHS-waiting-game/tree/main
```
- Move to folder

```
cd HygeiaOrg/NHS-waiting-game/tree/main
```

 - To open with VS code 

```
 code .
```
 - To open with jupyter notebook (or manually open using the jupyter notebook app)
```
jupyter notebook
```
