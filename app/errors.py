class VaccineError(Exception):
    def __str__(self) -> None:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, masks_to_buy: int) -> None:
        self.masks_to_buy = masks_to_buy

    def __str__(self) -> str:
        return f"Friends should buy {self.masks_to_buy} masks"
