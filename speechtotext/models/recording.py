class Recording():

    def __init__(self, id: int=None, time_to_recording: int=None, transcript: str=None, value: str=None, recording: str=None, experiment_id: int=None, user_id: int=None, exercise_id: int=None):  # noqa: E501
        """Recording - a model

        :param id: The id of this Recording.  # noqa: E501
        :type id: int
        :param recording: The recording of this Recording.  # noqa: E501
        :type recording: string
        :param time_to_recording: The time_to_recording of this Recording.  # noqa: E501
        :type time_to_recording: int
        :param transcript: The transcript of this Recording.
        :type transcript: str
        :param value: The value of this Recording.
        :type value: str
        :param experiment_id: The experiment_id of this Recording.  # noqa: E501
        :type experiment_id: int
        :param user_id: The user_id of this Recording.  # noqa: E501
        :type user_id: int
        :param exercise_id: The exercise_id of this Recording.  # noqa: E501
        :type exercise_id: int
        """

        self._id = id
        self._time_to_recording = time_to_recording
        self._transcript = transcript
        self._value = value
        self._recording = recording
        self._experiment_id = experiment_id
        self._user_id = user_id
        self._exercise_id = exercise_id

    @classmethod
    def from_dict(cls, dikt) -> 'Recording':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Recording of this Recording.  # noqa: E501
        :rtype: Recording
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Recording.


        :return: The id of this Recording.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Recording.


        :param id: The id of this Recording.
        :type id: int
        """

        self._id = id

    @property
    def recording(self) -> str:
        """Gets the recording of this Recording.


        :return: The recording of this Recording.
        :rtype: str
        """
        return self._recording

    @recording.setter
    def recording(self, recording: str):
        """Sets the recording of this Recording.


        :param recording: The recording of this Recording.
        :type recording: str
        """
        if recording is None:
            raise ValueError("Invalid value for `recording`, must not be `None`")  # noqa: E501

        self._recording = recording

    @property
    def time_to_recording(self) -> int:
        """Gets the time_to_recording of this Recording.


        :return: The time_to_recording of this Recording.
        :rtype: int
        """
        return self._time_to_recording

    @time_to_recording.setter
    def time_to_recording(self, time_to_recording: int):
        """Sets the time_to_recording of this Recording.


        :param time_to_recording: The time_to_recording of this Recording.
        :type time_to_recording: int
        """

        self._time_to_recording = time_to_recording

    @property
    def transcript(self) -> str:
        """Gets the transcript of this Recording.


        :return: The transcript of this Recording.
        :rtype: str
        """
        return self._transcript

    @transcript.setter
    def transcript(self, transcript: str):
        """Sets the transcript of this Recording.


        :param transcript: The transcript of this Recording.
        :type transcript: str
        """

        self._transcript = transcript

    @property
    def value(self) -> str:
        """Gets the value of this Recording.


        :return: The value of this Recording.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Recording.


        :param value: The value of this Recording.
        :type value: str
        """

        self._value = value

    @property
    def experiment_id(self) -> int:
        """Gets the experiment_id of this Recording.


        :return: The experiment_id of this Recording.
        :rtype: int
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id: int):
        """Sets the experiment_id of this Recording.


        :param experiment_id: The experiment_id of this Recording.
        :type experiment_id: int
        """

        self._experiment_id = experiment_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Recording.


        :return: The user_id of this Recording.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Recording.


        :param user_id: The user_id of this Recording.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def exercise_id(self) -> int:
        """Gets the exercise_id of this Recording.


        :return: The exercise_id of this Recording.
        :rtype: int
        """
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, exercise_id: int):
        """Sets the exercise_id of this Recording.


        :param exercise_id: The exercise_id of this Recording.
        :type exercise_id: int
        """

        self._exercise_id = exercise_id