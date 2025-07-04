

from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer
from .permissions import IsOwnerOrIsAdmin

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Expense/Income records.
    """
    serializer_class = ExpenseIncomeSerializer
    # IsAuthenticated ensures only logged-in users can access any endpoint.
    # IsOwnerOrIsAdmin is then checked for object-level operations (retrieve, update, destroy).
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsAdmin]

    def get_queryset(self):
        """
        This view should return a list of all the expense/income records
        for the currently authenticated user.
        A superuser should be able to see all records.
        """
        user = self.request.user
        if user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Assign the current user as the owner of the new record upon creation.
        """
        serializer.save(user=self.request.user)

