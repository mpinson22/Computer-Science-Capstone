################################################################
# Majors.py                                                    #
#                                                              #
# Defines parent and child classes for the different majors to #
# perform degree audits in the application                     #
################################################################

# super class Major
class Major(object):

    # constructor initializes object with requirements, and number of requirements
    def __init__(self):
        self.requirements = {}
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    # function used to go through a list of courses and decrement course requirements appropriately
    def runAudit(self, subjCode, courseNbr, requirements):
        # gets requirements from child class
        self.requirements = requirements
        # properly formats the query to align with requirements definition
        query = subjCode + str(courseNbr - (courseNbr % 100)) 

        
        if query in self.requirements.keys():
            # decrements to denote completion of the given course type
            self.requirements[query] -= 1

            # counts all courses of a particular type and level past what is required
            # as electives.
            if self.requirements[query] < 0: 
                self.requirements[query] = 0
                self.requirements['ELECTIVE'] -= 1
                # if all electives are fulfilled, additional courses do not count toward degree completion
                if self.requirements['ELECTIVE'] < 0:
                    self.requirements['ELECTIVE'] = 0

        # accounts for the cases where course requirements are for a particular subject code
        # and not at a particular x00 level
        elif subjCode in self.requirements.keys():
            self.requirements[subjCode] -= 1
            if self.requirements[subjCode] < 0:
                self.requirements[subjCode] = 0
                self.requirements['ELECTIVE'] -= 1
                if self.requirements['ELECTIVE'] < 0:
                    self.requirements['ELECTIVE'] = 0

        # counts all other courses as electives
        else:
            self.requirements['ELECTIVE'] -= 1
            if self.requirements['ELECTIVE'] < 0:
                self.requirements['ELECTIVE'] = 0

    # function to calculate the number of requirements from the requirements dictionary attribute
    # hard coding this value would create extra work when adding new degree requirements
    def calcNumReqs(self, requirements):
        for course in self.requirements:
            self.numReqs += self.requirements[course]


class Architecture(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'ARCH200': 3,
            'ARCH300': 4,
            'ARCH400': 3,
            'ARCH500': 5,
            'UD': 1,
            'URP': 2,
            'ARCH800': 2,
            'ELECTIVE': 5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)


class Education(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'EDUC200': 1,
            'EDUC300': 3,
            'EDUC400': 5,
            'EDUC500': 5,
            'EDUC600': 2,
            'EDUC700': 3,
            'EDUC800': 2,
            'ELECTIVE': 5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)

            
class Engineering(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'AEROSP':3,
            'BIOMEDE':3,
            'CEE':5,
            'CHE':3,
            'CLIMATE':3,
            'EECS':4,
            'ENGR':5,
            'ENTR':2,
            'IOE':2,
            'MATSCI':1,
            'MECHENG':2,
            'MFG':3,
            'NERS':3,
            'ROB':1,
            'SPACE':1,
            'TCHNCLCM':1,
            'ELECTIVE':3
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)


class EnvironmentalStudies(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'ENVIRON100':2,
            'ENVIRON200':2,
            'ENVIRON300':3,
            'ENVIRON400':4,
            'EAS500':5,
            'EAS600':2,
            'EAS700':1,
            'ELECTIVE':5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)

        
class Information(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'SI100':1,
            'SI200':1,
            'SI300':5,
            'SI400':3,
            'SI500':5,
            'SI600':4,
            'SI700':2,
            'ELECTIVE':5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)


class Kinesiology(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'AT':3,
            'HF200':1,
            'HF300':1,
            'HF400':2,
            'KINESLGY400':4,
            'KINESLGY500':2,
            'MOVESCI100':1,
            'MOVESCI200':2,
            'MOVESCI300':1,
            'MOVESCI400':3,
            'PHYSED':2,
            'SM100':1,
            'SM200':1,
            'SM300':2,
            'SM400':3,
            'SM500':1,
            'ELECTIVE':5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)

        
class Medicine(Major):
   
    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'ANATOMY':1,
            'BIOINF':3,
            'BIOLCHEM400':2,
            'BIOLCHEM500':4,
            'BIOLCHEM600':4,
            'BIOLCHEM700':1,
            'HHCR':1,
            'HUMGEN500':1,
            'HUMGEN600':3,
            'INTMED':2,
            'LHS600':2,
            'MICRBIOL':2,
            'NEUROSCI':3,
            'PATH':1,
            'PHRMACOL500':1,
            'PHRMACOL600':2,
            'PHYSIOL500':4,
            'ELECTIVE':5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)
        

class PerformingArts(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'ARTSADMIN':3,
            'COMP':1,
            'CONDUCT':1,
            'DANCE':4,
            'JAZZ':1,
            'MUSED':3,
            'MUSICOL':3,
            'MUSPERF':1,
            'MUSTHTRE':2,
            'PAT':2,
            'THTREMUS':2,
            'ELECTIVE':8
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)

        
class Nursing(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'HS':3,
            'NURS100':1,
            'NURS200':1,
            'NURS300':1,
            'NURS400':2,
            'NURS500':3,
            'NURS600':2,
            'NURS800':5,
            'NURS900':1,
            'PNE':3,
            'ELECTIVE':5    
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)


class Pharmacy(Major):

    # constructor
    def __init__(self):
        super().__init__()
        self.requirements = {
            'CPTS':1,
            'MEDCHEM':3,
            'PHARMACY200':1,
            'PHARMACY500':3,
            'PHARMACY600':2,
            'PHARMACY700':3,
            'PHARMSCI300':1,
            'PHARMSCI400':1,
            'PHARMSCI500':1,
            'PHARMSCI600':1,
            'PHARMSCI700':1,
            'PHARMSCI800':1,
            'ELECTIVE':5
        }
        self.numReqs = 0
        self.calcNumReqs(self.requirements)

    
    def runAudit(self, subjCode, courseNbr, requirements):
        super().runAudit(subjCode, courseNbr, self.requirements)

    
    def calcNumReqs(self, requirements):
        super().calcNumReqs(self.requirements)
