from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.db.models import Q


user1 = Jobseeker(user_id=1, name="Adrita Hossain Nakshi", email="adrita_99@yahoo.com", password="1234", thana="Boalia",
                  district="Rajshahi", division="Rajshahi", father_name="Dr. Md. Elias Hossain",
                  mother_name="Dr. Zennat Ferdousi", date_of_birth="1999-02-06", self_desc="I am a CS under-graduate. I love programmimg and I love computers too. Like Steve Jobs, I like to believe 'Everybody should learn to program a computer, because it teaches you how to think.'",
                  nationality="Bangladeshi", nid_number="12345678", field="Teaching", pref_sal="50000",
                  pref_job_ntr="Full-time", pref_org_type="Government", propic="propics_input/nakshi.jpg",
                  resume="resumes_input/nakshi.docx")
user1.save()
emp1 = Employer(user_id=2, name="Optimizely", email="optimizely@gmail.com", password="1234", district="Dhaka",
                division="Dhaka", org_type="NGO", establishment_year="2005")
emp1.save()
emp2 = Employer(user_id=3, name="Kona SL", email="kona@yahoo.com", password="1234", district="Kishoreganj", division="Dhaka",
                org_type="NGO", establishment_year="2001")
emp2.save()
emp3 = Employer(user_id=4, name="Data Edge Ltd", email="dataedge@gmail.com", password="1234", district="Sunamganj",
                division="Sylhet", org_type="NGO", establishment_year="1996")
emp3.save()
emp4 = Employer(user_id=5, name="Samsung", email="samsung@gmail.com", password="1234", district="Cox's Bazar",
                division="Chattogram", org_type="NGO", establishment_year="1981")
emp4.save()
emp5 = Employer(user_id=6, name="Intelligent Machines Limited", email="iml@gmail.com", password="1234",
                district="Rangpur", division="Rangpur", org_type="NGO", establishment_year="2015")
emp5.save()
emp6 = Employer(user_id=7, name="BEPRC", email="beprc@gmail.com", password="1234", district="Netrokona", division="Mymensingh",
                org_type="Government", establishment_year="1998")
emp6.save()
emp7 = Employer(user_id=8, name="Bangladesh Airforce", email="airbd@gmail.com", password="1234", district="Bogura",
                division="Rajshahi", org_type="Government", establishment_year="1975")
emp7.save()
contact1 = UserContact(user_contact_id=1, user_id=1, contact_no="01878046439")
contact1.save()
contact2 = UserContact(user_contact_id=2, user_id=1, contact_no="01718464397")
contact2.save()
jobpost1 = NewJobpost(jobpost_id=1, employer_id=emp1, title="Senior Software Engineer",
                      category="Research and Development", post_date="2022-06-28", deadline_date="2022-07-28",
                      salary=55000, required_experience=5, vacancies=2,
                      job_context="We are looking for a Sr. Software Engineer who will able to produce scalable software solutions. Selected Candidate will be the part of a cross-functional team that’s responsible for the full software development life cycle, from conception to deployment. As a Sr. Software Engineer, Candidate should be comfortable around both front-end and back-end coding languages, development frameworks and third-party libraries. Candidate should also be a team player with a knack for visual design and utility.",
                      job_nature="Full-time",
                      job_responsibilities="Work with development teams and product managers to ideate software solutions. Design client-side and server-side architecture",
                      edu_requirement="M.Sc/ B.Sc in Computer Science & Engineering or relevant degree from any reputed University",
                      additional_requirements="Work experience as a Full Stack Developer or similar role.",
                      application_process=" Email your CV from MY BDJOBS account.")
jobpost1.save()
jobpost2 = NewJobpost(jobpost_id=2, employer_id=emp2, title="Software Developer", category="Research and Development",
                      post_date="2022-06-26", deadline_date="2022-07-26", salary=50000, required_experience=3,
                      vacancies=2,
                      job_context="We are looking for a .NET Software Engineer to join our development team. The selected software engineers will get a chance to work with the latest technology stacks, exercising industry-standard principles & best practices to build scalable, high performance & robust software solutions.",
                      job_nature="Full-time",
                      job_responsibilities=" Good knowledge and understanding of ASP.NET Web Services, Restful Web APIs, OData, Entity Framework, Asynchronous Programming in C#, LINQ, Lambdas, Func, Action, Routing, Model Binding, MSSQL, MongoDb, etc.",
                      edu_requirement="Bachelor of Science (BSc) in Computer Science & Engineering, Bachelor of Computer Application (BCA) in Computer Applications",
                      additional_requirements="Age at least 24 years",
                      application_process="*Photograph must be enclosed with the resume.")
jobpost2.save()

jobpost3 = NewJobpost(jobpost_id=3, employer_id=emp3, title="Junior Software Engineer",
                      category="Teaching", post_date="2022-07-10", deadline_date="2022-08-10",
                      salary=50000, required_experience=3, vacancies=3,
                      job_context="AMBER GROUP invites applications for recruitment in the position:",
                      job_nature="Full-time",
                      job_responsibilities="Excellent working knowledge in Asp.Net, Asp.net MVC, WCF, Web API, LINQ, Entity Framework .Net Core",
                      edu_requirement="B.Sc in Computer Science or Software Engineering from any reputed university.",
                      additional_requirements="The applicants should have experience in the following business area(s): Software Company",
                      application_process=" Send your CV to resume@amber.com.bd")
jobpost3.save()
jobpost4 = NewJobpost(jobpost_id=4, employer_id=emp4, title="Software Developer ( Intern )", category="Programming",
                      post_date="2022-06-26", deadline_date="2022-07-26", salary=6000, required_experience=2,
                      vacancies=2,
                      job_context="In your CV you should share your leetcode.com username and GitHub user name.",
                      job_nature="Full-time",
                      job_responsibilities="Developing robust & user friendly secured web applications for managing the interchange of data between the server and the users.",
                      edu_requirement="Computer Science (CS)/ Bachelor of Science (B.Sc)/ Computer Science & Engineering (CSE)/ Software Engineering (SE) or any other relevant field.",
                      additional_requirements="Freshers are also encouraged to apply.",
                      application_process="*Photograph must be enclosed with the resume.")
jobpost4.save()
jobpost5 = NewJobpost(jobpost_id=5, employer_id=emp5, title="Software Engineer (Android)", category="Programming",
                      post_date="2022-06-23", deadline_date="2022-07-23", salary=60000, required_experience=1,
                      vacancies=2,
                      job_context="We are looking for passionate Software Engineers in the Android platform having strong knowledge and proven experience of a minimum 2 years in developing native Android apps. The ideal candidate will be responsible for developing high-quality applications. They will also be responsible for designing and implementing testable and scalable code.",
                      job_nature="Full-time",
                      job_responsibilities="Analyze product requirements and propose solutions to them.",
                      edu_requirement="Bachelor's degree in Computer Science or related field.",
                      additional_requirements="Deep Knowledge of Object-Oriented Design and Implementation.",
                      application_process="Send your CV to career@braincraftapps.com")
jobpost5.save()
jobpost6 = NewJobpost(jobpost_id=6, employer_id=emp6, title="Software Engineer (Asp.net Core, Angular)",
                      category="DevOps",
                      post_date="2022-07-02", deadline_date="2022-08-02", salary=45000, required_experience=2,
                      vacancies=2,
                      job_context="As a Software Engineer, you will be working with the team on different client projects and internal products expanding different platforms. You will work on implementing new features while taking ownership of the product or service. You will be working in a collaborative team with a supporting atmosphere. You will be able to strengthen your area of expertise to have shared success.",
                      job_nature="Full-time",
                      job_responsibilities="Work on feature development for different client projects and internal products.",
                      edu_requirement="Bachelor of Science (BSc) in CSE",
                      additional_requirements="Minimum 1 year of hands-on experience in software development.",
                      application_process="Send your CV to contact@creativitix.com")
jobpost6.save()
jobpost7 = NewJobpost(jobpost_id=7, employer_id=emp7, title="Software Engineer", category="DevOps",
                      post_date="2022-06-28", deadline_date="2022-08-28", salary=40000, required_experience=1,
                      vacancies=2,
                      job_context="We are looking for a Software Engineer to build functional and efficient server-client applications in Python. Responsibilities include participating in all phases of the software development lifecycle and be a good team player. If you’re a seasoned developer with a love for back-end technologies, have keen eye for detail and have problem-solving skills then we’d like to meet you.",
                      job_nature="Full-time",
                      job_responsibilities="Build efficient back-end features in Python",
                      edu_requirement="Bachelor of Science (BSc) in CSE in any reputed university.",
                      additional_requirements="Experience with Python frameworks (e.g., Django, Flask, FastAPI)",
                      application_process="Apply online")
jobpost7.save()
jobpost8 = NewJobpost(jobpost_id=8, employer_id=emp1, title="Junior Software Engineer",
                      category="DevOps", post_date="2022-07-08", deadline_date="2022-08-08",
                      salary=55000, required_experience=5, vacancies=2,
                      job_context="We are looking for a Sr. Software Engineer who will able to produce scalable software solutions. Selected Candidate will be the part of a cross-functional team that’s responsible for the full software development life cycle, from conception to deployment. As a Sr. Software Engineer, Candidate should be comfortable around both front-end and back-end coding languages, development frameworks and third-party libraries. Candidate should also be a team player with a knack for visual design and utility.",
                      job_nature="Full-time",
                      job_responsibilities="Bachelor of Science (BSc) in CSE in any reputed university.",
                      edu_requirement="M.Sc/ B.Sc in Computer Science & Engineering or relevant degree from any reputed University",
                      additional_requirements="Work experience as a Full Stack Developer or similar role.",
                      application_process=" Email your CV from MY BDJOBS account.")
jobpost8.save()
jobpost9 = NewJobpost(jobpost_id=9, employer_id=emp2, title="Senior Software Engineer (PHP - Laravel, Codeigniter)",
                      category="Programming",
                      post_date="2022-06-26", deadline_date="2022-07-26", salary=30000, required_experience=3,
                      vacancies=4,
                      job_context="Technical Experience : Codeigniter, Laravel, jQuery, Ajax, Vue.js, Mysql.",
                      job_nature="Full-time",
                      job_responsibilities="Analysis, Coding, Problem Solving and Team Leading.",
                      edu_requirement="Bachelor of Science (BSc)",
                      additional_requirements="Should have experience to guide software engineer.",
                      application_process="*Photograph must be enclosed with the resume.")
jobpost9.save()

jobpost10 = NewJobpost(jobpost_id=10, employer_id=emp3, title="Senior Application Security Engineer",
                       category="Programming", post_date="2022-07-10", deadline_date="2022-08-10",
                       salary=70000, required_experience=10, vacancies=4,
                       job_context="Job Grade: Senior Principal Officer to First Assistant Vice President",
                       job_nature="Full-time",
                       job_responsibilities="Perform Information Security Assessment of different ICT Systems, Services, Application and processes like Core Banking Applications, Payment Systems, Digital Banking Applications, Card Management System, SWIFT, Active Directory etc.",
                       edu_requirement="MSc/BSc in Computer Science, Information Systems, Information Technology or a related field from reputed University with No Third Division in academic records.",
                       additional_requirements="Minimum 10 year(s) working experience in relevant area",
                       application_process=" Apply online")
jobpost10.save()
jobpost11 = NewJobpost(jobpost_id=11, employer_id=emp4, title="Senior Software Engineer (Full Stack Java Developer)",
                       category="DevOps",
                       post_date="2022-06-29", deadline_date="2022-07-29", salary=4000, required_experience=2,
                       vacancies=5,
                       job_context="We are seeking an experienced, self-motivated Java engineer with 1+ years of experience in developing applications and 1+ technology experience.",
                       job_nature="Full-time",
                       job_responsibilities="Collaborates with the development team and initiates process improvements for new and existing systems.",
                       edu_requirement="Bachelor of Science (BSc) in CSE, IT, SE, Diploma in Engineering in Computer Science & Engineering",
                       additional_requirements="Requires 1+ years of hands-on experience in java and PL/SQL.",
                       application_process="*Photograph must be enclosed with the resume.")
jobpost11.save()
jobpost12 = NewJobpost(jobpost_id=12, employer_id=emp5, title=" Software Developer (Java) [MFSD- 20220616]",
                       category="Programming",
                       post_date="2022-06-23", deadline_date="2022-07-23", salary=45000, required_experience=1,
                       vacancies=2,
                       job_context="Developers need to compile detailed technical documentation and user assistance material, requiring excellent written communication.",
                       job_nature="Full-time",
                       job_responsibilities="Coding, testing and troubleshooting so that developed software performs as per requirements",
                       edu_requirement="Bachelor of Science (BSc) in CSE, Post Graduate Diploma (PGD) in Computer Science & Engineering",
                       additional_requirements="Age 25 to 40 years",
                       application_process="Apply online")
jobpost12.save()
jobpost13 = NewJobpost(jobpost_id=13, employer_id=emp6,
                       title="Senior Test Engineer/Test Engineer (Software), Capital Market Solutions",
                       category="Security",
                       post_date="2022-07-05", deadline_date="2022-08-05", salary=65000, required_experience=2,
                       vacancies=2,
                       job_context="Test Engineer - We are seeking an experienced, self-motivated test engineer with 1+ years of experience in software testing and for Senior Test Engineer- Test engineer with 1+ years of experience in developing software and 3+ software testing experience. ",
                       job_nature="Full-time",
                       job_responsibilities="and internal products.",
                       edu_requirement="Bachelor of Science (BSc) in CSE",
                       additional_requirements="Minimum 1 year of hands-on experience in software development.",
                       application_process="Send your CV to contact@creativitix.com")
jobpost13.save()
jobpost14 = NewJobpost(jobpost_id=14, employer_id=emp7,
                       title="Senior Test Engineer/Test Engineer (Software), Capital Market Solutions",
                       category="DevOps",
                       post_date="2022-06-30", deadline_date="2022-08-30", salary=50000, required_experience=3,
                       vacancies=3,
                       job_context="We are looking for a Software Engineer to build functional and efficient server-client applications in Python. Responsibilities include participating in all phases of the software development lifecycle and be a good team player. If you’re a seasoned developer with a love for back-end technologies, have keen eye for detail and have problem-solving skills then we’d like to meet you.",
                       job_nature="Full-time",
                       job_responsibilities="Automates test coverage per platform capabilities and requirements. Establishes and maintains continuous build and integration testing on applicable platforms and assists with manual system and integration testing efforts.",
                       edu_requirement="Bachelor of Computer Science & Engineering",
                       additional_requirements="Ability to communicate clearly and concisely, both orally and in writing.",
                       application_process="*Photograph must be enclosed with the resume.")
jobpost14.save()


skill1 = Skill(skill_id =1, skill_name="c++", gap_between_consecutive_attempts=30)
skill1.save()

question1 = Question(question_id=1, skill_id=skill1, question_text="The library function exit( ) causes an exit from - ",
                     optionA="The program in which it occurs",
                     optionB="The function in which it occurs",
                     optionC="The block in which it occurs",
                     optionD="The loop in which it occurs",
                     answer="The program in which it occurs",
                     mark =10,
                     time_limit="00:01:30")
question1.save()
class postViewsets(viewsets.ModelViewSet):
    # def list(self,request):
    #     posts = Jobpost.objects.all()
    #     serializer = postSerializer(posts, many=True)
    #     return Response(serializer.data)
    queryset = Jobpost.objects.all()
    serializer_class = postSerializer


class postViewsets_for_jobpost(viewsets.ModelViewSet):
    queryset = NewJobpost.objects.all()
    serializer_class = NewPostSerializer
    cat = ""
    org = ""
    loc = ""
    keyword = ""
    nature = ""

    @action(methods=['post', 'get'], detail=False, url_path='searchinput')
    def follow(self, request):

        if request.method == 'POST':
            print(request.data['category'])
            print(request.data['organization'])
            print(request.data['location'])
            print(request.data['keyword'])
            print(request.data['nature'])
            postViewsets_for_jobpost.cat = request.data['category']
            postViewsets_for_jobpost.org = request.data['organization']
            postViewsets_for_jobpost.loc = request.data['location']
            postViewsets_for_jobpost.keyword = request.data['keyword']
            postViewsets_for_jobpost.nature = request.data['nature']
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            if postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),
                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 Q(job_nature=postViewsets_for_jobpost.nature), (
                                                             Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                         category__icontains=postViewsets_for_jobpost.keyword)
                                                             | Q(
                                                         job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                         job_nature=postViewsets_for_jobpost.keyword)
                                                             | Q(
                                                         job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                         edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                             | Q(
                                                         additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                         application_process__icontains=postViewsets_for_jobpost.keyword)
                                                             | Q(
                                                         employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                         employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                             | Q(
                                                         employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                         employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                             | Q(
                                                         employer_id__name__icontains=postViewsets_for_jobpost.keyword)))

            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(employer_id__division=postViewsets_for_jobpost.loc),
                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 Q(job_nature=postViewsets_for_jobpost.nature), (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),
                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 Q(job_nature=postViewsets_for_jobpost.nature))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),
                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),

                                                 Q(job_nature=postViewsets_for_jobpost.nature), (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),

                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 Q(job_nature=postViewsets_for_jobpost.nature), (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc),
                    Q(employer_id__org_type=postViewsets_for_jobpost.org),
                    Q(job_nature=postViewsets_for_jobpost.nature))
            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc),
                    Q(employer_id__org_type=postViewsets_for_jobpost.org),
                    (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc),

                    Q(job_nature=postViewsets_for_jobpost.nature), (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__org_type=postViewsets_for_jobpost.org),
                    Q(job_nature=postViewsets_for_jobpost.nature), (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),
                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org))

            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),

                                                 Q(job_nature=postViewsets_for_jobpost.nature))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),

                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 Q(job_nature=postViewsets_for_jobpost.nature))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc),
                                                 (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),

                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org),
                                                 (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),

                                                 Q(job_nature=postViewsets_for_jobpost.nature), (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))
            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc),
                    Q(employer_id__org_type=postViewsets_for_jobpost.org))


            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc),
                    (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))

            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(

                    Q(job_nature=postViewsets_for_jobpost.nature), (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))

            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc),
                    (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))

            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(

                    Q(employer_id__org_type=postViewsets_for_jobpost.org),
                    (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))

            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(

                    Q(job_nature=postViewsets_for_jobpost.nature), (
                            Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                            | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                            | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword)))

            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 Q(employer_id__division=postViewsets_for_jobpost.loc))




            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),

                                                 Q(employer_id__org_type=postViewsets_for_jobpost.org))


            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),

                                                 Q(job_nature=postViewsets_for_jobpost.nature))


            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat),
                                                 (
                                                         Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     category__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     job_nature=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     application_process__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                                                     employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                                                         | Q(
                                                     employer_id__name__icontains=postViewsets_for_jobpost.keyword)))


            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc != "":
                objs = NewJobpost.objects.filter(
                    Q(employer_id__division=postViewsets_for_jobpost.loc)
                )


            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org != "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(employer_id__org_type=postViewsets_for_jobpost.org))
            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature != "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(

                    Q(job_nature=postViewsets_for_jobpost.nature))

            elif postViewsets_for_jobpost.cat == "" and postViewsets_for_jobpost.keyword != "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(
                    Q(title__icontains=postViewsets_for_jobpost.keyword) | Q(
                        category__icontains=postViewsets_for_jobpost.keyword)
                    | Q(
                        job_context__icontains=postViewsets_for_jobpost.keyword) | Q(
                        job_nature=postViewsets_for_jobpost.keyword)
                    | Q(
                        job_responsibilities__icontains=postViewsets_for_jobpost.keyword) | Q(
                        edu_requirement__icontains=postViewsets_for_jobpost.keyword)
                    | Q(
                        additional_requirements__icontains=postViewsets_for_jobpost.keyword) | Q(
                        application_process__icontains=postViewsets_for_jobpost.keyword)
                    | Q(
                        employer_id__org_type__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__thana__icontains=postViewsets_for_jobpost.keyword)
                    | Q(
                        employer_id__district__icontains=postViewsets_for_jobpost.keyword) | Q(
                        employer_id__division__icontains=postViewsets_for_jobpost.keyword)
                    | Q(
                        employer_id__name__icontains=postViewsets_for_jobpost.keyword))
            elif postViewsets_for_jobpost.cat != "" and postViewsets_for_jobpost.keyword == "" and postViewsets_for_jobpost.nature == "" and postViewsets_for_jobpost.org == "" and postViewsets_for_jobpost.loc == "":
                objs = NewJobpost.objects.filter(Q(category=postViewsets_for_jobpost.cat))

            else:
                objs = NewJobpost.objects.all()
            serializer = NewPostSerializer(objs, many=True)
            return Response({
                'status': status.HTTP_204_NO_CONTENT,
                'data': serializer.data,


            })




class usercontactViewsets(viewsets.ModelViewSet):
    queryset = UserContact.objects.all()
    serializer_class = usercontactSerializer

class jobseekerViewsets(viewsets.ModelViewSet):
    queryset = Jobseeker.objects.all()
    serializer_class = jobseekerSerializer
    isdetails=False
    email=""
    password=""

    @action(methods=['post', 'get'], detail=False, url_path='matchuser')
    def match(self,request):
        if request.method == 'POST':

            jobseekerViewsets.isdetails=True
            jobseekerViewsets.email=request.data['email']
            jobseekerViewsets.password=request.data['password']
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            if jobseekerViewsets.isdetails==True:
                print(jobseekerViewsets.email)
                print(jobseekerViewsets.password)
                objs = Jobseeker.objects.filter(email=jobseekerViewsets.email,password=jobseekerViewsets.password)
                str=""
                if len(objs)==1:
                    str="success"
                else :
                    str="fail"
                serializer = jobseekerSerializer(objs, many=True)
                jobseekerViewsets.isdetails = False
                return Response({
                    'status': status.HTTP_204_NO_CONTENT,
                    'data': serializer.data,
                    'response':str,

                })
            else :
                jobseekerViewsets.isdetails = False
                return Response({
                    'status': status.HTTP_204_NO_CONTENT,
                    'data': None,
                    'response': "not_submitted",

                })





class recoViewsets(viewsets.ModelViewSet):
    queryset = NewJobpost.objects.all()
    serializer_class = NewPostSerializer


