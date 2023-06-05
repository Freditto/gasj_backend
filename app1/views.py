from django.shortcuts import render

from django.conf import settings
from authUser.models import User
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def InsertGas(request):
    data = request.data
    gas = Gas.objects.create(
        name=data['name'],
        user=User.objects.get(id=data['user_id']),
        weight=data['weight'],
    )
    gas.save()
    g = Gas.objects.get(id=gas.id)
    gas = GasStatus.objects.create(
        gas=g,
        percent="100",
    )
    code = "GAS" + "{:04}".format(g.id)
    g.gas_code = code
    g.save()
    response = {'message': "success"}
    return Response(response)


# {
#     "name": "tigo",
#     "user_id": 1,
#     "weight": 20,
# }


@api_view(["POST"])
@permission_classes([AllowAny])
def InsertGasStatus(request):
    data = request.data
    gas = GasStatus.objects.create(
        gas=Gas.objects.get(id=data['gas_id']),
        percent=str(data['percent']),
    )
    gas.save()
    all = GasStatus.objects.all()
    if gas.id>=2:
        gas_b = GasStatus.objects.get(id=gas.id-1)
        gas_b.is_active = False
        gas_b.save()
    else:
        pass

    response = {'change': "success"}
    return Response(response)


# {
#     "gas_id": 1,
#     "percent": 20,
# }

@api_view(["GET"])
@permission_classes([AllowAny])
def ResetGas(request, gas_id):
    gas = GasStatus.objects.create(
        gas=Gas.objects.get(id=gas_id),
        percent=100,
    )
    gas.save()
    # all = GasStatus.objects.all()
    if gas.id >= 2:
        gas_b = GasStatus.objects.get(id=gas.id - 1)
        gas_b.is_active = False
        gas_b.save()
    else:
        pass

    response = {'change': "success"}
    return Response(response)


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def setQuestions(request, vac_id):
#     # added by a specific company which hiring
#     data = request.data
#     for s in data:
#         question = Question.objects.create(
#             question=s['question'],
#             is_checkable=s['is_checkable'],
#             vacancy_id=JobVacancy.objects.get(id=vac_id)
#         )
#         question.save()
#         q = Question.objects.get(id=question.id)
#         for d in s['answer']:
#             answer = Answer.objects.create(answer=d['answer'], question_id=q, is_correct=d['is_correct'])
#             answer.save()
#
#     response = {"sms": 'success'}
#     return Response(response)
#
#
# # data = [
# #     {"question": "bra bra", "is_checkable": false,
# #      "answer":[
# #          {"answer": "yes", "is_correct": true},
# #          {"answer": "no", "is_correct": false}
# #         ]
# #      },
# #     {"question": "bra bra", "is_checkable": false,
# #      "answer":[
# #          {"answer": "yes", "is_correct": true},
# #          {"answer": "no", "is_correct": false}
# #         ]
# #      }
# # ]
#
#
# @api_view(["GET"])
# @permission_classes([AllowAny])
# def getMultipleChoice(request, vac_id):
#     vacancy = JobVacancy.objects.get(id=vac_id)
#     questions = Question.objects.values('id', 'question').filter(vacancy_id=vacancy)
#     data = []
#     for q in questions:
#         que = Question.objects.get(id=q['id'])
#         ans = Answer.objects.values('id', 'answer').filter(question_id=que)
#         qs = {'id': q['id'], 'question': q['question'], 'answer': ans}
#         data.append(qs)
#     try:
#         default_question = Question.objects.values('id', 'question').filter(is_checkable=True)
#         x = [e for e in default_question]
#         for q in x:
#             que = Question.objects.get(id=q['id'])
#             ans = Answer.objects.values('id', 'answer').filter(question_id=que)
#             qs = {'id': q['id'], 'question': q['question'], 'answer': ans}
#             data.append(qs)
#
#     except:
#         pass
#     response = {"data": data}
#     return Response(response)
#
#
# # {
# #     "hiring_id": 1
# # }
#
#
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def setAnswer(request, seeker_id):
#     # kata = Kata.objects.get(id=request.data['kata_id'])
#     seeker = SeekerProfile.objects.get(id=seeker_id)
#     data = request.data
#     fail = []
#     pas = []
#     d_q = []
#     for r in data:
#         question = Question.objects.get(id=r['question_id'])
#         if not question.is_checkable:
#             if len(Answer.objects.filter(Q(id=r['answer_id']) and Q(question_id=question) and Q(is_correct=True)) == 1):
#                 pas.append(1)
#             else:
#                 fail.append(1)
#         else:
#             d_q.append(r)
#
#     for r2 in d_q:
#         is_corr = False
#         ans = Answer.objects.get(id=r2['answer'])
#         try:
#             if ans.answer == seeker.education_level:
#                 is_corr = True
#             else:
#                 pass
#         except:
#             pass
#
#         try:
#             if ans.answer == seeker.country:
#                 is_corr = True
#             else:
#                 pass
#         except:
#             pass
#
#         try:
#             if ans.answer == seeker.gender:
#                 is_corr = True
#             else:
#                 pass
#         except:
#             pass
#
#         if is_corr:
#             pas.append(1)
#         else:
#             fail.append(1)
#
#     percent = 100 * len(pas) / (len(pas) + len(fail))
#     if percent < 50:
#         status = "failed"
#     else:
#         status = "pass"
#
#     data = {'percent': percent, 'status': status}
#     response = {"data": data}
#     return Response(response)
#
#
# # [
# #     {'question_id': 1, 'answer_id': 1},
# #     {'question_id': 2, 'answer_id': 5},
# #     {'question_id': 3, 'answer_id': 6},
# #     {'question_id': 4, 'answer_id': 11},
# # ]
#
@api_view(["GET"])
@permission_classes([AllowAny])
def GetGases(request, user_id):
    data = Gas.objects.values('id', 'gas_code', 'weight', 'name', 'created_at').filter(user=User.objects.get(id=user_id))
    d = [e for e in data]
    d2 = []
    print(d)
    for d in data:
        # current = GasStatus.objects.get(gas=Gas.objects.get(id=d['id']))
        d3 = {
            'id': d['id'],
            'gas_code': d['gas_code'],
            'name': d['name'],
            'created_at': d['created_at'],
            'percent': 30,
            'weight': d['weight']
            # 'percent': current.percent,
        }
        d2.append(d3)
    return Response(d2)


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def GetCurrentGasStatus(request, gas_id):
#     gas = Gas.objects.get(id=gas_id)
#     data = Gas.objects.values('id', 'gas_code', 'name', 'created_at').all()
#     d = [e for e in data]
#     return Response(d)

#
#
# @api_view(["GET"])
# @permission_classes([AllowAny])
# def VacancyInfo(request, vac_id):
#     data = JobVacancy.objects.get(id=vac_id)
#     req = Requirement.objects.values('id', 'requirement').filter(vacancy_id=data)
#     d = {
#         'id': data.company,
#         'jobTitle': data.jobTitle,
#         'duration': data.duration,
#         'requirements': req
#     }
#     return Response(d)
#
#
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def DefaultQuestion(request):
#     # added by a specific company which hiring
#     data = request.data
#     for s in data:
#         question = Question.objects.create(
#             question=s['question'],
#             is_checkable=s['is_checkable']
#             # vacancy_id=JobVacancy.objects.get(id=vac_id)
#         )
#         question.save()
#         q = Question.objects.get(id=question.id)
#         for d in s['answer']:
#             answer = Answer.objects.create(answer=d['answer'], question_id=q, is_correct=d['is_correct'])
#             answer.save()
#
#     response = {"sms": 'success'}
#     return Response(response)
#
#
# # [
# #     {"question": "Is your country?", "is_checkable": true,
# #      "answer":[
# #          {"answer": "Tanzania", "is_correct": false},
# #          {"answer": "Kenya", "is_correct": false},
# #          {"answer": "Uganda", "is_correct": false}
# #      ]
# #      },
# #     {"question": "Is your gender?", "is_checkable": true,
# #      "answer":[
# #          {"answer": "male", "is_correct": false},
# #          {"answer": "female", "is_correct": false}
# #         ]
# #      },
# #     {"question": "Is your level of education?", "is_checkable": true,
# #      "answer":[
# #          {"answer": "ordinary diploma", "is_correct": false},
# #          {"answer": "bachelor degree", "is_correct": false},
# #          {"answer": "masters", "is_correct": false},
# #         ]
# #      }
# # ]
#
#
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def addRequirement(request):
#     job = JobVacancy.objects.get(id=request.data['vac_id'])
#     req = Requirement.objects.create(requirement=request.data['requirement'], job=job)
#     req.save()
#     response = {"save": True}
#     return Response(response)
#
# # {
# #     "requirement": "bra bra",
# #     "vac_id": 1
# # }
#
#
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def getRequirements(request, vac_id):
#     job = JobVacancy.objects.get(id=vac_id)
#     req = Requirement.objects.values('requirement').filter(job=job)
#     return Response(req)
#
