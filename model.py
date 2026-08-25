class Wheel:
    """
    класс для представления шины.
    """
    def CountDiameter(width: float, 
                      percent: float, 
                      discDiameterInInch: int) -> float:
        """Расчет диаметра шины.

        Args:
            width (float): ширина шины.
            percent (float): процентное отношение высоты боковины к ширине шины.
            discDiameter (int): диаметр диска (в дюймах).

        Returns:
            float: диаметр шины в мм.
        """

        # высота боковины
        height = width * (percent / 100)

        # диаметр диска в мм
        discDiameterInMM = discDiameterInInch * 25.4

        return 2 * height + discDiameterInMM