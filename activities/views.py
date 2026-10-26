
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentDb
from .serializers import StudentSerializer


class StudentListCreateView(APIView):

    def get(self, request):
        students = StudentDb.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

class StudentSummaryView(APIView):

    def get(self, request):
        students = StudentDb.objects.all()

        total_entries = students.count()
        total_hours = sum(student.hours for student in students)

        student_hours = {}

        for student in students:
            name = student.student_name
            student_hours[name] = (
                student_hours.get(name, 0) + student.hours
            )

        most_active_user = None

        if student_hours:
            most_active_user = max(
                student_hours, key=student_hours.get
            )

        data = {
            "total_entries": total_entries,
            "total_hours": total_hours,
            "most_active_user": most_active_user
        }

        return Response(data, status=status.HTTP_200_OK)

