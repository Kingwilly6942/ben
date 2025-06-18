class GoCard:
    """Represents a GoCard account that records transactions."""
    def __init__(self, initial_balance: float = 0.0):
        self.balance = float(initial_balance)
        self.transactions = []  # store transaction descriptions in order

    def ride(self, amount: float):
        if amount <= 0:
            raise ValueError("Ride cost must be positive")
        cost, discounted = self.apply_discount(amount)
        if cost > self.balance:
            raise ValueError("Insufficient funds for ride costing %.2f" % amount)
        self.balance -= cost
        label = self.discount_label(discounted)
        desc = f"Ride ${amount:.2f}" + (f" ({label})" if label else "")
        self.record_transaction(desc)

    def top_up(self, amount: float):
        if amount <= 0:
            raise ValueError("Top up amount must be positive")
        self.balance += amount
        self.record_transaction(f"Top up ${amount:.2f}")

    def get_balance(self) -> float:
        return self.balance

    def record_transaction(self, desc: str):
        self.transactions.append(desc)

    def statement(self) -> str:
        lines = [*self.transactions, f"Balance ${self.balance:.2f}"]
        return "\n".join(lines)

    # Methods intended for overriding by subclasses
    def apply_discount(self, amount: float) -> tuple[float, bool]:
        """Return (cost, discounted). Base class applies no discount."""
        return amount, False

    def discount_label(self, discounted: bool) -> str:
        return "5% discount" if discounted else ""


class RegularGoCard(GoCard):
    """GoCard with a discount after every 10 full-price rides."""
    def __init__(self, initial_balance: float = 0.0):
        super().__init__(initial_balance)
        self.ride_counter = 0
        self.discount_rides_remaining = 0

    def apply_discount(self, amount: float) -> tuple[float, bool]:
        if self.discount_rides_remaining > 0:
            self.discount_rides_remaining -= 1
            return amount * 0.95, True
        else:
            self.ride_counter += 1
            if self.ride_counter == 10:
                self.discount_rides_remaining = 5
                self.ride_counter = 0
            return amount, False

    def discount_label(self, discounted: bool) -> str:
        return "5% discount" if discounted else ""


class PensionerGoCard(GoCard):
    """GoCard with permanent pensioner discount on rides."""
    def apply_discount(self, amount: float) -> tuple[float, bool]:
        return amount * 0.95, True

    def discount_label(self, discounted: bool) -> str:
        return "5% pensioner discount" if discounted else ""


class Person:
    """Represents a person holding a GoCard."""
    def __init__(self, name: str, card: GoCard):
        self.name = name
        self.card = card
